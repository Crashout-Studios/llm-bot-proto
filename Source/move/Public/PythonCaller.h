#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "PythonCaller.generated.h"

UCLASS()
class YOURPROJECTNAME_API APythonCaller : public AActor
{
    GENERATED_BODY()

public:
    // Sets default values for this actor's properties
    APythonCaller();

protected:
    // Called when the game starts or when spawned
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void Tick(float DeltaTime) override;

    // Blueprint callable function
    UFUNCTION(BlueprintCallable, Category = "Python")
    FString CallPythonFunction(const FString& Input);
};