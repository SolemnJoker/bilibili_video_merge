#!env python
import sys,os,json,subprocess,re

def getFileInfo(entryFile):
    try:
        with open(entryFile) as f:
            info = json.loads(f.read())

        return info["title"].replace(" ","-"), info["page_data"]["part"].replace(" ","-"),info["page_data"]["page"]
    except Exception as identifier:
        print("open",entryFile,"  error:",identifier)

def makeOutdir(inFolder,outFolder):
    parentFolder = os.path.dirname(inFolder)
    inName = os.path.basename(inFolder)
    outPath = parentFolder+ "/"+ inName+"-" + outFolder
    if not os.path.exists(outPath):
        os.makedirs(outPath)
    return outPath

def calcTime(timeStr):
    tl = timeStr.split(":")
    return float(tl[0])*3600+float(tl[1])*60 +float(tl[3])
 
   
def mergeVideo(videoFile,audioFile,outFile):
    try:
        print('############## start merge: ' + outFile)
       
        cmd = "ffmpeg -i "+ videoFile+" -i "+ audioFile +" -strict -2 -f mp4 " +outFile
        print(cmd)
        p = subprocess.Popen(cmd,
                             shell=True, stdout=subprocess.PIPE)
        videoTime = 1
        while p.poll() is None:
            output = p.stdout.readline().decode('utf-8')
            # if output != "":
            #     if videoTime == 1 and output.count("Duration") != 0:
            #         videoTime = calcTime(re.findall("\\d\\d:\\d\\d:\\d\\d\\.\\d\\d",output));
            #     elif output.count("frame") !=0:
            #         curtime  = calcTime(re.findall("\\d\\d:\\d\\d:\\d\\d\\.\\d\\d",output));
            #         print("----proccess:"+str(curtime*100.0/videoTime) +"%")
            #     else:
            #         print(output)

                        
                
    except Exception as e:
        print("run cmd error:")
        print(e)

        
def mergeFolder(folder):
    for subDir in os.listdir(folder):
        if os.path.isdir(folder+"/"+subDir):
            title,part,page = getFileInfo(folder+"/"+subDir +"/entry.json")
            outFile = makeOutdir(folder,title) + "/"+str(page)+"-"+part + ".mp4"
            mergeVideo(folder+"/"+subDir +"/"+"80/video.m4s",
                       folder+"/"+subDir +"/"+"80/audio.m4s",
                      outFile)
            
            
            
        
if __name__ == "__main__":
    folder=sys.argv[1]
    mergeFolder(folder)

