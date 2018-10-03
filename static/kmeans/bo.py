import numpy as np
from bokeh.plotting import figure,ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.models import  Slider, Button, Label
from bokeh.palettes import Spectral11
from skimage.external import tifffile as T


img_o=T.imread('C:/Users/UserXX/Desktop/Image_Sequence.tif')

frames=list(range(0,img_o.shape[0]))
img=np.flip(img_o,1)



source = ColumnDataSource(data=dict(image=[img[0,:,:]]))


p_img = figure(x_range=(0,1388), y_range=(0, 1040))
label = Label(x=1.1, y=18, text=str(frames[0]), text_font_size='70pt', text_color='#eeeeee')
p_img.add_layout(label)
im=p_img.image(image='image', x=0, y=0, dw=1388, dh=1040, source=source, palette="Spectral11")

slider = Slider(start=frames[0], end=frames[-1], value=frames[0],step=1, title="Frame")

def animate_update():
    frame = slider.value + 1
    if frame > frames[-1]:
        frame = frames[0]
    slider.value = frame

ds=im.data_source    

def slider_update(attr, old, new):

    new_data=dict()
    frame = slider.value
    label.text = str(frame)
    new_data['image']=[img[frame,:,:]]
    ds.data= new_data



slider.on_change('value', slider_update)


def animate():
    if button.label == '► Play':
        button.label = '❚❚ Pause'
        curdoc().add_periodic_callback(animate_update, 200)
    else:
        button.label = '► Play'
        curdoc().remove_periodic_callback(animate_update)

button = Button(label='► Play', width=60)
button.on_click(animate)

l = layout([[p_img],[slider,button],], sizing_mode='scale_width')
curdoc().add_root(l)
curdoc().title = "Image_sequence"