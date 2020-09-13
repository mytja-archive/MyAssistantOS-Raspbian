import requests
import json

def getRidOf(text):
    q = text.lower()
    q = q.replace("g", "")
    q = q.replace("u", "")
    q = q.replace("i", "")
    q = q.replace("n", "")
    q = q.replace("e", "")
    q = q.replace("a", "")
    q = q.replace("_", "")
    q = q.replace("b", "")
    q = q.replace("t", "")
    q = q.replace("l", "")
    q = q.replace("s", "")
    q = q.replace("v", "")
    q = q.replace(".", "")
    return q

def checkForVersions(stability, currentTag):
    i = True
    r = requests.get("https://api.github.com/repos/mytja/MyAssistantOS-Raspbian/releases")
    y = r.json()
    for item in y:
        if (i != False):
            i = False
            version = item["tag_name"]
            author = item["author"]["login"]
            target = item["target_commitish"]
            description = item["body"]

    ver = int(getRidOf(version))
    curver = int(getRidOf(currentTag))
    
    #print(ver)
    #print(curver)
    
    if (ver < curver):
        update = "y"
    else:
        update = "n"

    end = {
        "update": update,
        "branch": target,
        "version": version,
        "description": description,
        "publisher": author,
        "ver": ver
    }

    finalJSON = json.dumps(end)

    return finalJSON

checkForVersions("beta", "1.0.1")
