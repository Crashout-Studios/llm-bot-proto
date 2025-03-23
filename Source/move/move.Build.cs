// Fill out your copyright notice in the Description page of Project Settings.

using UnrealBuildTool;
using System.IO;

public class move : ModuleRules
{
	public move(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
	
		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore" });

		PrivateDependencyModuleNames.AddRange(new string[] {  });



        string PythonScriptPath = Path.Combine(ModuleDirectory, "llmcallcode.py");
        string OutputPath = Path.Combine("$(BinaryOutputDir)", "move", "llmcallcode.py");
        RuntimeDependencies.Add(OutputPath, PythonScriptPath);

        // Lägg till Python-sökvägar
        string PythonPath = "C:/Users/jonat/AppData/Local/Programs/Python/Python313"; // Ersätt med din Python-sökväg

        // Lägg till Python include-mapp
        PublicIncludePaths.Add(Path.Combine(PythonPath, "include"));

        // Lägg till Python biblioteksmapp
        PublicSystemLibraryPaths.Add(Path.Combine(PythonPath, "libs"));

        // Lägg till Python-biblioteket med fullständig sökväg
        string PythonLibrary = Path.Combine(PythonPath, "libs", "python313.lib");
        PublicAdditionalLibraries.Add(PythonLibrary);
        // Uncomment if you are using Slate UI
        // PrivateDependencyModuleNames.AddRange(new string[] { "Slate", "SlateCore" });

        // Uncomment if you are using online features
        // PrivateDependencyModuleNames.Add("OnlineSubsystem");

        // To include OnlineSubsystemSteam, add it to the plugins section in your uproject file with the Enabled attribute set to true
    }
}
