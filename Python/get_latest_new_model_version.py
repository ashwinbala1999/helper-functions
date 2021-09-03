import os


# expects path to saved_models dir
def get_model_versions(path):
    versions = [int(item) for item in os.listdir(path)]
    
    if len(versions)==0:
        return {
            "next": 1
        }
    else:
        return {
            "cur": max(versions),
            "next": max(versions)+1
        }
