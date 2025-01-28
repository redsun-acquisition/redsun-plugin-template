from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):

    # TODO: add entry point context for controllers
    def hook(self, context: dict) -> dict:
        """Add hook to update context based on user's input."""
        if context["plugin_type"] == "Controller":
            context["module_import"] = "controller"
            context["class_baseline"] = "MyController"
            context["entry_point_group"] = "controllers"
        else:
            context["module_import"] = "model"
            context["class_baseline"] = "MyModel"
            context["entry_point_group"] = "models"
        context["config_info"] = context["class_baseline"] + "Info" 
        context["entry_point_value"] = context["class_baseline"].lower()
        context["entry_point_cfg_value"] = context["class_baseline"].lower() + "_config"
        return context
