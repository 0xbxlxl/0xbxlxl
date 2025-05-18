from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Dataset
from .forms import ProjectForm, DatasetForm
from .data_processing import fetch_geo_data, preprocess_geo_data, generate_heatmap, generate_pca, generate_umap
from django.http import JsonResponse


def index(request):
    """Home page of the application."""
    return render(request, 'genexpresso/index.html')


@login_required
def projects(request):
    """Display all projects of the logged-in user."""
    projects = Project.objects.filter(owner=request.user).order_by('-date_added')
    return render(request, 'genexpresso/projects.html', {'projects': projects})


@login_required
def project(request, project_id):
    """Display a single project and its datasets."""
    project = get_object_or_404(Project, id=project_id)

    if project.owner != request.user:
        raise Http404("You do not have permission to view this project.")

    datasets = project.dataset_set.order_by('-date_added')
    return render(request, 'genexpresso/project.html', {'project': project, 'datasets': datasets})


@login_required
def new_project(request):
    """Add a new project."""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('genexpresso:projects')
    else:
        form = ProjectForm()

    return render(request, 'genexpresso/new_project.html', {'form': form})


@login_required
def edit_project(request, project_id):
    """Edit an existing project."""
    project = get_object_or_404(Project, id=project_id)

    if project.owner != request.user:
        raise Http404("You do not have permission to edit this project.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('genexpresso:projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'genexpresso/edit_project.html', {'project': project, 'form': form})


@login_required
def delete_project(request, project_id):
    """Delete a project."""
    project = get_object_or_404(Project, id=project_id)

    if project.owner != request.user:
        raise Http404("You do not have permission to delete this project.")

    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('genexpresso:projects')


@login_required
def new_dataset(request, project_id):
    """Add a new dataset to a project."""
    project = get_object_or_404(Project, id=project_id)

    if project.owner != request.user:
        raise Http404("You do not have permission to add datasets to this project.")

    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            new_dataset = form.save(commit=False)
            new_dataset.project = project
            new_dataset.save()
            messages.success(request, 'Dataset created successfully!')
            return redirect('genexpresso:project', project_id=project.id)
    else:
        form = DatasetForm()

    return render(request, 'genexpresso/new_dataset.html', {'form': form, 'project': project})


@login_required
def edit_dataset(request, dataset_id):
    """Edit an existing dataset."""
    dataset = get_object_or_404(Dataset, id=dataset_id)
    project = dataset.project

    if project.owner != request.user:
        raise Http404("You do not have permission to edit this dataset.")

    if request.method == 'POST':
        form = DatasetForm(request.POST, instance=dataset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dataset updated successfully!')
            return redirect('genexpresso:project', project_id=project.id)
    else:
        form = DatasetForm(instance=dataset)

    return render(request, 'genexpresso/edit_dataset.html', {'form': form, 'project': project, 'dataset': dataset})


@login_required
def delete_dataset(request, dataset_id):
    """Delete a dataset."""
    dataset = get_object_or_404(Dataset, id=dataset_id)
    project = dataset.project

    if project.owner != request.user:
        raise Http404("You do not have permission to delete this dataset.")

    dataset.delete()
    messages.success(request, 'Dataset deleted successfully!')
    return redirect('genexpresso:project', project_id=project.id)


@login_required
def analyze_dataset(request, dataset_id):
    """Analyze a dataset by generating visualizations."""
    dataset = get_object_or_404(Dataset, id=dataset_id)
    project = dataset.project

    if project.owner != request.user:
        raise Http404("You do not have permission to analyze this dataset.")

    # Fetch and preprocess data
    try:
        geo_data, group_labels = fetch_geo_data(dataset.geo_id)
        if not geo_data:
            messages.error(request, 'GEO dataset not found.')
            return redirect('genexpresso:project', project_id=project.id)
        
        processed_data = preprocess_geo_data(geo_data)

    # Generate visualizations
        heatmap_html = generate_heatmap(processed_data, group_labels)
        pca_html = generate_pca(processed_data, group_labels)
        umap_html = generate_umap(processed_data, group_labels)

        context = {
            'dataset': dataset,
            'project': project,
            'visualizations': {
                'heatmap': heatmap_html,
                'pca': pca_html,
                'umap': umap_html,
            },
        }
        return render(request, 'genexpresso/analyze_dataset.html', context)
    
    except Exception:
        messages.error(request, f'GEO type is not known, try checking your GEO ID.')
        return redirect('genexpresso:project', project_id=project.id)


def logout_page(request):
    """Log the user out and redirect to the home page."""
    username = request.user.username
    logout(request)
    return render(request,'genexpresso/logout_page.html', {'username': username})


def help_page(request):
    """Guide for user to use the website."""
    return render(request, 'genexpresso/help_page.html')

def loading_page(request, dataset_id):
    """Loading page while data is being analyzed."""
    context = {'dataset_id': dataset_id}  
    return render(request, 'genexpresso/loading_page.html', context)


def check_status(request, dataset_id):
    # to check if the analysis is done (replace with actual tracking logic)
    analysis_done = False  # Replace this with real logic
    return JsonResponse({"status": "done" if analysis_done else "processing"})


