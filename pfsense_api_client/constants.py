""" constant values """

RESPONSE_CODES = {
    200 : "API call succeeded",
    400 : "An error was found within your requested parameters",
    401 : "API client has not completed authentication or authorization successfully",
    403 : "The API endpoint has refused your call. Commonly due to your access settings found in System > API",
    404 : "Either the API endpoint or requested data was not found",
    500 : "The API endpoint encountered an unexpected error processing your API request",
}
