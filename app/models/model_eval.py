
def sorted_functions_by_mse(models, selected_models, complexity_level, x0, y0):
    functions = []

    # Filter away None values which indicate inability to fit
    models = [model for model in models if model.get_model_name() in selected_models]

    for model in models:
        func = model.get_best_fit(complexity_level, x0, y0)
        if func:
            functions.append(func)
    
    # Sort models by mean squared error
    functions.sort(key=lambda func: func.mse)
    return functions

def get_all_names(models):
    names = []
    for model in models:
        names.append(model.get_model_name())
    return names