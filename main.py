from ultralytics import YOLO

model = YOLO('/teamspace/studios/this_studio/models/best.pt')

results = model.predict('/teamspace/studios/this_studio/input_video/08fd33_4.mp4', save=True)
print(results[0])
print('###############################################')
for box in results[0].boxes:
    print(box)