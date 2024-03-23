import math

class BubbleCursor:
    def __init__(self, canvas, objects, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = 40
        self.canvas = canvas
        self.objects = objects
        self.cursor_size = 7
        self.distances = []

        # create a area cursor: a horizontal segment, a vertical segment, and a circle
        self.cursor_tag_circle = self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius,
                                                         y + self.radius, fill="gray", outline="gray", width=0)
        self.canvas.tag_lower(self.cursor_tag_circle)  # move the cursor's circle to bottom level

        self.cursor_tag_horizontal = self.canvas.create_line(x - self.cursor_size, y, x + self.cursor_size, y,
                                                             fill='black', width=2)
        self.cursor_tag_vertical = self.canvas.create_line(x, y - self.cursor_size, x, y + self.cursor_size,
                                                           fill='black', width=2)

        self.selected_object = -1  # no object has been selected

    def update_cursor(self, x, y):
        # according to the (x, y), update the area cursor
        self._determine_selected_object(x, y)
        self.canvas.coords(self.cursor_tag_circle, x - self.radius, y - self.radius, x + self.radius, y + self.radius)
        self.canvas.coords(self.cursor_tag_horizontal, x - self.cursor_size, y, x + self.cursor_size, y)
        self.canvas.itemconfig(self.cursor_tag_horizontal, fill="black", width=2)
        self.canvas.coords(self.cursor_tag_vertical, x, y - self.cursor_size, x, y + self.cursor_size)
        self.canvas.itemconfig(self.cursor_tag_vertical, fill="black", width=2)

    def get_selected_object(self):  # return the index of the selected object in the object list
        return self.selected_object

    def _determine_selected_object(self, x, y):
        # shortest_intersecting_distance = 0
        # closest_object = -1  # no object has been selected

        # Calculate the distances of all objects from the current (x,y) positions
        # append the distances to the list self.distances
        # finds the shortest distance and the second shortest distance for the bubble cursor radius.

        for i in range(len(self.objects)):
            distance = math.hypot(self.objects[i].x - x, self.objects[i].y - y)
            self.distances.append(distance)

        shortest_intersecting_distance = min(self.distances)

        closest_object = self.distances.index(shortest_intersecting_distance)
        self.distances.sort()
        # with the use of sort(), second shortest can be found

        second_shortest_distance = self.distances[1]

        IntD = second_shortest_distance - self.objects[i].radius
        ConD = shortest_intersecting_distance + self.objects[i].radius

        self.radius = min(IntD, ConD)

        # list is cleared here for it to be used again
        self.distances.clear()

        self.selected_object = closest_object  # find the selected object