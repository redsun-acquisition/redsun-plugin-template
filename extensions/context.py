from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):

    # TODO: add entry point context for controllers
    def hook(self, context: dict) -> dict:
        """Add hook to update context based on user's input."""
        if context["plugin_type"] == "Controller":
            context["module_import"] = "controller"
            context["entry_point_group"] = "controllers"
            if context["add_widget"]:
                context["widget_module_import"] = "widget"
                context["widget_entry_point_group"] = "widgets"
        elif context["plugin_type"] == "Model":
            context["module_import"] = "model"
            context["entry_point_group"] = "models"
        else:
            context["module_import"] = "widget"
            context["entry_point_group"] = "widgets"
        context["config_info"] = context["class_baseline"] + "Info" 
        context["entry_point_value"] = context["class_baseline"].lower()
        context["entry_point_cfg_value"] = context["class_baseline"].lower() + "_config"
        
        return context
