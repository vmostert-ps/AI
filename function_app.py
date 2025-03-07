import azure.functions as func
import logging
from src.leanix_utils.survey_utils import SurveyUtils
import traceback
app = func.FunctionApp()

@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.FUNCTION)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP trigger for processing survey responses."""
    try:
        req_body = req.get_json()

        # Initialize SurveyUtils
        survey_utils = SurveyUtils()
            
        # Process the survey response
        result = survey_utils.process_survey_response(req_body)
        
        return func.HttpResponse(
            result["message"],
            status_code=result["status_code"]
        )
        
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(
            f"Internal server error: {str(traceback.format_exc())}",
            status_code=500
        )