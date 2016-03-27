#!/usr/local/bin/python
#导入turtle模块
import turtle

turtle.speed(1)

#显示turtle图形窗口
turtle.showturtle()

#turtle.setheading(angle)
turtle.setheading(10)

#绘制字符串
turtle.write("hello world")

#向前走100
turtle.forward(100)

#向后走100
#turtle.backward(100)
#设置x坐标
#turtle.setx(x)
#设置y坐标
#turtle.sety(y)
#返回0,0
#turtle.home()

#右转
turtle.right(90)

turtle.forward(100)

#改变颜色
turtle.color("red")

#
#turtle.dot(d, color)
turtle.dot(50, "green")
#
turtle.pensize(3)

#左转
turtle.left(90)

turtle.forward(100)

#抬起笔
turtle.penup()

#将笔移动到x,y坐标处 goto(x,y)
turtle.goto(20,20)

#放下笔
turtle.pendown()

#
#turtle.circle(r, ext, step)
turtle.circle(50, 360, 5)
#画圆
turtle.circle(50)

while True:
	pass

#None
