from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):

    def hook(self, context: dict) -> dict:
        """Add hook to update context based on user's input."""
        if context["plugin_type"] == "Model":
            if context["plugin_model_type"] == "Detector":
                if context["mm_support"]:
                    context["plugin_base"] == "ExEngineMMCameraModel"
                else:
                    context["plugin_base"] == "ExEngineDetectorModel"
            else: # motor model
                if context["plugin_motor_type"] == "Single":
                    if context["mm_support"]:
                        context["plugin_base"] == "ExEngineMMSingleMotorModel"
                    else:
                        context["plugin_base"] == "ExEngineSingleMotorModel"
                else: # dual-axis (XY) motor
                    if context["mm_support"]:
                        context["plugin_base"] == "ExEngineMMDoubleMotorModel"
                    else:
                        context["plugin_base"] == "ExEngineDoubleMotorModel"       
        return context
    