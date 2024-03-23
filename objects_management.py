import math
import random

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class ObjectManager:
    def __init__(self, canvas, window_width, window_height, object_num, object_radius):
        self.canvas = canvas
        self.window_width = window_width
        self.window_height = window_height
        self.object_num = object_num  # object number
        self.object_radius = object_radius
        self.objects = []  # store all objects
        self.object_tag_in_canvas = []  # store the tag of the objects in canvas
        self.last_selected_object_index = 0

    def update_object_mouse_click(self, object_index):
        # object_tag is used to find the object in canvas, so that we can update the object
        if object_index >= 0:  # a target has been selected
            object_tag = self.object_tag_in_canvas[object_index]
            self.canvas.itemconfig(object_tag, fill="yellow", outline="gray",
                                   width=6)  # Yellow indicates the selected target

    def update_object(self, object_index):
        if object_index >= 0:  # a target has been selected
            if self.last_selected_object_index != object_index:
                if self.last_selected_object_index == 0:
                    last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
                    # update object according to their tag
                    self.canvas.itemconfig(last_object_tag, fill="blue", width=0)
                    self.last_selected_object_index = object_index
                elif self.last_selected_object_index == 1:
                    last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
                    # update object according to their tag
                    self.canvas.itemconfig(last_object_tag, fill="red", width=0)
                    self.last_selected_object_index = object_index
                else:
                    last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
                    # update object according to their tag
                    self.canvas.itemconfig(last_object_tag, fill="green", width=0)
                    self.last_selected_object_index = object_index

                # object_tag is used to find the object in canvas, so that we can update the object
                object_tag = self.object_tag_in_canvas[object_index]
                self.canvas.itemconfig(object_tag, fill="red", outline="gray",
                                       width=6)  # red indicates the selected target
        else:  # no target has been selected, we change the previously selected target to green
            if self.last_selected_object_index == 0:
                last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
                self.canvas.itemconfig(last_object_tag, fill="blue", width=0)
                self.last_selected_object_index = object_index
            elif self.last_selected_object_index == 1:
                last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
                self.canvas.itemconfig(last_object_tag, fill="red", width=0)
                self.last_selected_object_index = object_index
            else:
                last_object_tag = self.object_tag_in_canvas[self.last_selected_object_index]
                # update object according to their tag
                self.canvas.itemconfig(last_object_tag, fill="green", width=0)
                self.last_selected_object_index = object_index

    def paint_objects(self):
        # the first item in the objects list is the start and the second is the target.
        # accordingly, the circles are created with color.
        for t in self.objects:
            if t == self.objects[0]:
                tag = self.canvas.create_oval(t.x - t.radius, t.y - t.radius, t.x + t.radius, t.y + t.radius,
                                              fill="blue", outline="blue", width=0)
            elif t == self.objects[1]:
                tag = self.canvas.create_oval(t.x - t.radius, t.y - t.radius, t.x + t.radius, t.y + t.radius,
                                              fill="red", outline="red", width=0)
            else:
                tag = self.canvas.create_oval(t.x - t.radius, t.y - t.radius, t.x + t.radius, t.y + t.radius,
                                              fill="green", outline="green", width=0)
            # add object's tag to the list, so they can be accessed according to their tag
            # note that objects are indexed in the same order in both objects and object_tag_in_canvas lists
            self.object_tag_in_canvas.append(tag)

    def generate_random_targets(self):
        i = 0

        # The start circle is created with the center (60, 740) and appended to the "Objects" list

        start_circle = Circle(60, 740, 20)
        self.objects.append(start_circle)

        distance = 512
        while True:
            # The Target circle is created with a hypotenuse of 512 pixels with the center of the start circle.
            new_target = Circle(random.randint(self.object_radius, self.window_width - self.object_radius),
                                random.randint(self.object_radius, self.window_height - self.object_radius),
                                self.object_radius)

            hyp = math.hypot((new_target.x - start_circle.x), (new_target.y - start_circle.y))

            if hyp == distance:
                target = new_target

                self.objects.append(target)
                #print("circle= ", target, "hyp= ", hyp)
                break

        while i < self.object_num:
            # 20 random distractors are built here.
            new_object = Circle(random.randint(self.object_radius, self.window_width - self.object_radius),
                                random.randint(self.object_radius, self.window_height - self.object_radius),
                                self.object_radius)
            overlap = False

            # Random distractors are created by checking the other objects in the Object list to avoid overlapping.

            for j in self.objects:
                if self.check_two_targets_overlap(new_object, j):
                    overlap = True
                    break

            if not overlap:  # if the new object does not overlap with others, add it to the objects list.
                self.objects.append(new_object)
                i += 1

        self.paint_objects()
        return self.objects

    def check_two_targets_overlap(self, t1, t2):
        if math.hypot(t1.x - t2.x, t1.y - t2.y) > (t1.radius + t2.radius):
            return False
        else:
            return True
