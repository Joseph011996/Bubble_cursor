import math

class NormalCursor:
    def __init__(self, canvas, objects, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = 20
        self.canvas = canvas
        self.objects = objects

        self.selected_object = -1  # no object has been selected

    def update_cursor(self, x, y):
        # according to the (x, y), update the area cursor
        self._determine_selected_object(x, y)

    def get_selected_object(self):  # return the index of the selected object in the object list
        return self.selected_object

    def _determine_selected_object(self, x, y):
        closest_object = -1  # no object has been selected

        # find the closest target overlapping the area cursor
        for i in range(len(self.objects)):
            # when the pointer is within the circle's radius it can be selected.
            distance = math.hypot(self.objects[i].x - x, self.objects[i].y - y)
            if distance <= self.radius:
                closest_object = i

        self.selected_object = closest_object  # find the selected object