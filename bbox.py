import cv2


class BBox:

    def __init__(self, class_index, bbox_n, original_size):
        self.class_index = class_index
        self.bbox_n = bbox_n
        self.original_size = original_size

    @staticmethod
    def from_label_line(line: str, original_size):
        class_index, cxn, cyn, cwn, chn = line.split()
        class_index = int(class_index)
        cxn, cyn, cwn, chn = tuple(map(float, (cxn, cyn, cwn, chn)))

        xn = cxn - cwn / 2
        yn = cyn - chn / 2
        wn = cwn
        hn = chn

        bbox_n = (xn, yn, wn, hn)
        return BBox(class_index, bbox_n, original_size)

    @staticmethod
    def from_label_file(file_path, original_size):
        with open(file_path, 'r', encoding='utf-8') as fp:
            for line in fp:
                yield BBox.from_label_line(line.strip(), original_size)

    @property
    def xywh(self):
        width, height = self.original_size
        xn, yn, wn, hn = self.bbox_n

        x = xn * width
        y = yn * height
        w = wn * width
        h = hn * height

        return x, y, w, h

    @property
    def xywhn(self):
        return tuple(self.bbox_n)

    def plot(self, img):
        x, y, w, h = map(int, self.xywh)
        _img = img.copy()
        _img = cv2.rectangle(_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return _img
