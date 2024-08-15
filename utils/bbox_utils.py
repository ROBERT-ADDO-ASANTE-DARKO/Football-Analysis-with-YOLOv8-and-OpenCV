def get_center_of_bbox(bbox):
    x_center = int((bbox[0] + bbox[2]) // 2)
    y_center = int((bbox[1] + bbox[3]) // 2)
    return x_center, y_center
    #x1, y1, x2, y2 = bbox
    #return int((x1 + x2)/2), int((y1 + y2)/2)

def get_bbox_width(bbox):
    return bbox[2] - bbox[0]