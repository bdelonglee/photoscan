# How to launch
# ./photoscan-pro/photoscan.sh -r "path_to_script.py"



import PhotoScan
import os

doc = PhotoScan.Document()

path="/home/ben/Downloads/photoscan/monument/3_views/"  #path to the image folder

# chunk = PhotoScan.Chunk()
chunk = doc.addChunk()
chunk.label = "New Chunk"

# doc.chunks.add(chunk)

photos_list = os.listdir(path)
tofList = []
for tof in photos_list:
    tofList.append(path+"/"+tof)

print (tofList)

# for photo_name in tofList:     #adding all files from the folder
chunk.addPhotos(tofList)

#Align Photos
chunk.matchPhotos(accuracy = PhotoScan.HighAccuracy)
# chunk.matchPhotos(accuracy = "high", preselection="disabled", filter_mask=False, point_limit=40000)
chunk.alignCameras()   
# chunk.alignPhotos()   

#Build Geometry
# chunk.buildDepth(quality="high", p1=40, p2=2000, gpu_mask=1, cpu_cores_inactive=1)
chunk.buildDenseCloud(quality=PhotoScan.UltraQuality)
chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation,face_count=PhotoScan.HighFaceCount, vertex_colors=True)
chunk.buildUV(mapping=PhotoScan.GenericMapping)
chunk.buildTexture(blending=PhotoScan.MosaicBlending, size=4096)

chunk.exportModel(path="/home/ben/Downloads/photoscan/scriptTest/GEO.obj", format=PhotoScan.ModelFormat.ModelFormatOBJ, texture=True, normals=True, colors=True, texture_format=PhotoScan.ImageFormat.ImageFormatJPEG)
doc.save("/home/ben/Downloads/photoscan/scriptTest/project_test.psx")
