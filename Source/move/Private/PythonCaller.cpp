#include "PythonCaller.h"
#include "Python.h"

// Sets default values
APythonCaller::APythonCaller()
{
    // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
    PrimaryActorTick.bCanEverTick = true;
}

// Called when the game starts or when spawned
void APythonCaller::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void APythonCaller::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
}

FString APythonCaller::CallPythonFunction(const FString& Input)
{
    // Initialize the Python interpreter
    Py_Initialize();

    // Convert FString to std::string
    std::string InputStr = TCHAR_TO_UTF8(*Input);

    // Python code to call the function
    const char* PythonCode = R"(
import sys
sys.path.append((r"C:\Users\jonat\OneDrive\Dokument\pvk")  # Add the path to your Python script
from llmcallcode import get_ai_response
response = get_ai_response('{}')
)";

    // Format the Python code with the input
    std::string FormattedCode = std::vformat(PythonCode, std::make_format_args(InputStr));

    // Execute the Python code
    PyRun_SimpleString(FormattedCode.c_str());

    // Get the result from Python
    PyObject* PyResponse = PyObject_GetAttrString(PyImport_AddModule("__main__"), "response");
    FString Response = FString(UTF8_TO_TCHAR(PyUnicode_AsUTF8(PyResponse)));

    // Clean up
    Py_Finalize();

    return Response;
}