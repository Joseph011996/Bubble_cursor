The bubble cursor is an object pointing technique. It is rendered as a semi-transparent circular area cursor. A small crosshair is drawn in the centre of the bubble cursor indicating the current location of the standard pointer. 
At any point, it finds the closest clickable element to the cursor and makes it selectable. The bubble cursor is faster than point cursors and other object pointing techniques. 
The algorithm proposed in [1] is used to continuously update the radius of the bubble cursor, such that there is always exactly one target within its activation area.
