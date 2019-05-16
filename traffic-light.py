root = Tk()
lights = [Frame(root, width=200, height=200) for _ in range(3)]
 
colors = (
    ('#FF0000', '#FFFF00', '#00FF00'),
    ('#440000', '#444400', '#004400'),
)
 
def update(counter=0):
    for i, a in enumerate(lights):
        a['bg'] = colors[i != counter % 3][i]

    root.after(500, update, counter + 1)
 
for a in lights:
    a.pack()
 
update()
root.mainloop()