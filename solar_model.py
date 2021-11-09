# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    for i in space_objects:
		for j in space_objects:
			r = ((space_objects[i] - space_objects[j])**2 + (space_objects[i] - space_objects[j])**2)**0.5
			if r != 0:
				space_objects[i].Fx += gravitational_constant*space_objects[i].m*space_objects[j].m*(space_objects[j].x-space_objects[i].x)/(r**3)
				space_objects[i].Fy += gravitational_constant*space_objects[i].m*space_objects[j].m*(space_objects[j].y-space_objects[i].y)/(r**3)
			else:
				space_objects[i].Fx += 0
				space_objects[i].Fy += 0
		


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    body.ax = body.Fx/body.m
    body.ay = body.Fy/body.m
    body.Vx += body.ax*dt
    body.Vy += body.ay*dt
    body.x += body.Vx*dt
    body.y += body.Vy*dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
