def setup():
    size(400,400)
    textSize(80)
    textAlign(CENTER)
def draw():
    text("K", width/2-40, (height/3)*2)
    fill(0,102,153)
    text("W", width/2+40, (height/3)*2)
    fill(153,102,0)
    print(keyCode)
    #print(hex(get(mouseX,mouseY)))
    if keyPressed:
        if keyCode == 39:
            fill(255,0,0)
        print(keyCode)
        if key == "k":
            fill(255,0,255)
    
        
        
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255, 100)
    s.noStroke()
    s.vertex(50,(height/4)*3)
    s.vertex(width/2+20, (height/4)*3-30)
    s.vertex(width/2-20, (height/4)*3)
    s.vertex(width/2+20, (height/4)*3+30)
    s.vertex(width/2+20, (height/4)*3)
    s.endShape(CLOSE)
    shape(s, 25, 25)
