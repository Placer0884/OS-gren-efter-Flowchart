
def s(var):

    yes = ["Yes", "yes", "Y", "y", "Yes!", "yes!", "Ja", "ja"]
    no = ["No", "no", "N", "n", "No!", "no!", "Nej", "nej"]
    stop = ["Stop", "stop", "Stop!", "stop!"]
    cancel = ["Cancel", "cancel"]

    if var in yes:
        var = "yes"

    if var in no:
        var = "no"

    if var == stop:
        var = "stop"

    if var in cancel:
        var = "cancel"


    return var


#---------------------------------------------------------------------------------------------#


def sf(var):

    yes = ["Yes", "yes", "Y", "y", "Yes!", "yes!"]
    no = ["No", "no", "N", "n", "No!", "no!"]
    stop = ["Stop", "stop", "Stop!", "stop!"]
    cancel = ["Cancel", "cancel"]

    if var in yes or var in no or var in stop or var in cancel:

        for i in range(len(yes)):
            if var == yes[i]:
                var = "yes"


        for i in range(len(no)):
            if var == no[i]:
                var = "no"

        for i in range(len(stop)):
            if var == stop[i]:
                var = "stop"

    else:
        var = "error"


    return var
