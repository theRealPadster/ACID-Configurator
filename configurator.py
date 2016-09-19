# Credits:
#
# tutorials from http://developer.gnome.org/gnome-devel-demos/stable/tutorial.py.html.en
# get_colour() function by android_808 on the Arch Linux forums
# help from Satyajit Sahoo and Bilal Akhtar, #gnome on irc.freenode.net
# big thanks to Sean Davis for helping getting things lined up right

from gi.repository import Gtk
from gi.repository import Gdk
import os
import sys
 
class MyWindow(Gtk.ApplicationWindow):
    # constructor for a Gtk.ApplicationWindow
    def __init__(self, app):
        Gtk.Window.__init__(self, title="ACID Configurator", application=app)
        self.set_default_size(640, 355)
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)
 
        self.installDir=os.getenv('HOME')+"/.themes/ACID/"
 
    	# errorLabel
        errorLabel = Gtk.Label()
        # set the text of the label
        errorLabel.set_text("Please move your ACID installation to ~/.themes/ACID")
 
    	# errorButton
        errorButton = Gtk.Button()
        # with a label
        errorButton.set_label("Okay")
        # connect the signal "clicked" emitted by the button
        # to the callback function do_clicked
        errorButton.connect("clicked", self.do_clicked_errorButton)
 
        errorButtonBox = Gtk.ButtonBox.new(Gtk.Orientation.VERTICAL)
        errorButtonBox.set_spacing(15)
        errorButtonBox.set_layout(Gtk.ButtonBoxStyle.SPREAD)
        errorButtonBox.add(errorLabel)
        errorButtonBox.add(errorButton)
 
        # test if the theme is in the correct location
        if os.path.isfile(self.installDir + "gnome-shell/gnome-shell.css"):
            print ("'~/.themes/ACID/gnome-shell/gnome-shell.css' is a file. Congratulations.")
        else:
            print ("'~/.themes/ACID/gnome-shell/gnome-shell.css' isn't a file. Please move your ACID installation there.")
            self.set_default_size(430, 50)
            self.add(errorButtonBox) # TODO - fix errors
               
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
       
        # create an image
        self.previewImage = Gtk.Image()
        # set the content of the image as the file filename.png
        self.previewImage.set_from_file(self.installDir+"gnome-shell/assets/acid-preview.svg")
        self.previewImage.yalign = 0
        self.previewImage.ypad = 0
       
        hbox.pack_start(self.previewImage, False, False, 0)
       
        # create an image
        self.labelImage = Gtk.Image()
        # set the content of the image as the file filename.png
        self.labelImage.set_from_file(self.installDir+"gnome-shell/assets/acid-label.svg")
        self.labelImage.set_alignment(0, 0)
       
        vbox.pack_start(self.labelImage, False, False, 0)
 
        # read colour from current gnome-shell.css file
        shellFile = open(self.installDir + "gnome-shell/gnome-shell.css", 'r')
        colourLine = shellFile.readline() # read the first line
        shellFile.close() # close the file
        colourString = colourLine[2:9] # grab the colour from the line
        os.environ["oldcolour"] = colourString #set oldcolour var
        # split up colourString into individual r, g, and b values
        hexR = colourString[1:3]
        hexG = colourString[3:5]
        hexB = colourString[5:7]
        # convert individual hex values to decimal
        rgbR = int(hexR, 16)
        rgbG = int(hexG, 16)
        rgbB = int(hexB, 16)
        # convert individual decimal values to percents
        self.percR = rgbR/float(255) # need to use the float or it returns an integer
        self.percG = rgbG/float(255)
        self.percB = rgbB/float(255)
       
        button_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
       
        leftButtonBox = Gtk.ButtonBox.new(Gtk.Orientation.VERTICAL)
        leftButtonBox.set_spacing(15)
        leftButtonBox.set_layout(Gtk.ButtonBoxStyle.SPREAD)
       
        rightButtonBox = Gtk.ButtonBox.new(Gtk.Orientation.VERTICAL)
        rightButtonBox.set_spacing(15)
        rightButtonBox.set_layout(Gtk.ButtonBoxStyle.SPREAD)
       
        button_hbox.pack_start(leftButtonBox, True, True, 0)
        button_hbox.pack_end(rightButtonBox, True, True, 0)
       
        # a single line entry
        self.export_entry = Gtk.Entry()
        # emits a signal when the Enter key is pressed, connected to the
        # callback function linked to the exportButton
        self.export_entry.connect("activate", self.do_clicked_exportButton)
        self.export_entry.set_placeholder_text("Name current config...")
        self.export_entry.set_tooltip_text("e.g. 'red' will make a theme called 'ACID-red'")
       
        leftButtonBox.add(self.export_entry)
       
        # exportButton
        exportButton = Gtk.Button()
        # with a label
        exportButton.set_label("Export")
        exportButton.set_tooltip_text("Export current config to its own theme")
        # connect the signal "clicked" emitted by the button
        # to the callback function do_clicked
        exportButton.connect("clicked", self.do_clicked_exportButton)
       
        rightButtonBox.add(exportButton)
 
        # colourLabel
        colourLabel = Gtk.Label()
        # set the text of the label
        colourLabel.set_text("Highlight colour")
        colourLabel.set_justify(Gtk.Justification.RIGHT) # TODO - doesn't work?
       
        leftButtonBox.add(colourLabel)
 
        # a colorbutton (which opens a dialogue window in
        # which we choose a color)
        self.colourButton = Gtk.ColorButton()
        # set the default colour to whatever the current colour is
        self.colour = Gdk.RGBA()
        self.colour.red = self.percR
        self.colour.green = self.percG
        self.colour.blue = self.percB
        self.colour.alpha = 1.0
        self.colourButton.set_rgba(self.colour)
        # choosing a colour in the dialogue window emits a signal
        self.colourButton.connect("color-set", self.on_colour_chosen)
       
        rightButtonBox.add(self.colourButton)
 
        # resetButton
        resetButton = Gtk.Button()
        # with a label
        resetButton.set_label("    Reset    ")
        resetButton.set_tooltip_text("Reset ACID to the default green colour")
        # connect the signal "clicked" emitted by the button
        # to the callback function do_clicked
        resetButton.connect("clicked", self.do_clicked_resetButton)
       
        leftButtonBox.add(resetButton)
        leftButtonBox.set_child_non_homogeneous(resetButton, True)
 
    # applyButton
        applyButton = Gtk.Button()
        # with a label
        applyButton.set_label("    Apply    ")
        applyButton.set_tooltip_text("Start using new highlight colour")
        # connect the signal "clicked" emitted by the button
        # to the callback function do_clicked
        applyButton.connect("clicked", self.do_clicked_applyButton)
 
        rightButtonBox.add(applyButton)
 
        # add the grid to the window
        vbox.pack_end(button_hbox, True, True, 0)
 
        #set focus on self.colourButton so that placeholder text shows up in entry box
        self.colourButton.grab_focus()
 
        os.environ["acidcolour"] = '#'+self.get_colour(self.colourButton) #set acidcolour var to the current colour
 
        print ("oldcolour=" + os.environ["oldcolour"] + "/acidcolour=" + os.environ["acidcolour"])
 
    # the content of the entry is used to write in the terminal
    #####def cb_activate(self, entry):
        # retrieve the content of the widget
    #####name = self.export_entry.get_text()
    # print it in a nice form in the terminal
    #####print "Your entry is " + name + "!"
 
    # callback function connected to the signal "clicked" of the errorButton
    def do_clicked_errorButton(self, errorButton):
        sys.exit(0) #quit
 
    # callback function connected to the signal "clicked" of the exportButton
    def do_clicked_exportButton(self, exportButton):
        name = self.export_entry.get_text() # the text inside the enty box
        # if entry box is empty, don't continue
        if name == "":
            print ("Oh, you idiot!")
        else:
            print ("You clicked the exportButton!")
            os.putenv('exportname', name) #set exportname var
            print ("*Just set $exportname to whatever is in export_name_box*")
            os.system(self.installDir+'configurator/export.sh')
            print ("*Just ran export.sh*")
 
    # callback function connected to the signal "clicked" of the applyButton
    def do_clicked_applyButton(self, applyButton):
    #print "1 - oldcolour=" + os.environ["oldcolour"] + "/acidcolour=" + os.environ["acidcolour"]
        if os.environ["acidcolour"] == os.environ["oldcolour"]:
            print ("acidcolour and oldcolour are the same")
        else:
            print ("You clicked the applyButton!")
            os.system(self.installDir+'configurator/colour-changer.sh')
            print ("*Just ran colour-changer.sh*")
            os.system(self.installDir+'configurator/apply.sh')
            print ("*Just ran apply.sh*")
            os.environ["oldcolour"] = '#'+self.get_colour(self.colourButton) #set oldcolour var to the new colour
            #print "2 - oldcolour=" + os.environ["oldcolour"] + "/acidcolour=" + os.environ["acidcolour"]
 
    # callback function connected to the signal "clicked" of the resetButton
    def do_clicked_resetButton(self, resetButton):
        print ("You clicked the resetButton!")
        print ("oldcolour=" + os.environ["oldcolour"])
        if os.environ["oldcolour"] == '#a6e028': #if already default
            print ("oldcolour is the default green colour")
        else: #if not set at default, make it so
            os.putenv('acidcolour','#a6e028') #reset acidcolour var
            print ("*Just reset $acidcolour to #a6e028*")
            os.system(self.installDir+'configurator/colour-changer.sh')
            print ("*Just ran colour-changer.sh*")
            os.system(self.installDir+'configurator/apply.sh')
            print ("*Just ran apply.sh*")
        #always reload image, reset colourbox, and oldcolour
        self.previewImage.set_from_file(self.installDir+"gnome-shell/assets/acid-preview.svg") #reload image
        self.labelImage.set_from_file(self.installDir+"gnome-shell/assets/acid-label.svg") #reload image
        self.colour.red = 166/float(255)
        self.colour.green = 224/float(255)
        self.colour.blue = 40/float(255)
        self.colourButton.set_rgba(self.colour)
        os.environ["oldcolour"] = '#'+self.get_colour(self.colourButton)#set oldcolour var to the new colour
 
    # if a new colour is chosen, we print it as #rrggbb in the terminal
    def on_colour_chosen(self, colourButton):
        print ("You chose #" + self.get_colour(self.colourButton))
        os.environ["acidcolour"] = '#'+self.get_colour(self.colourButton) #set acidcolour var to what's in the colourButton
        os.system(self.installDir+'configurator/colour-changer.sh') # change theme to box colour
        print ("*Just ran colour-changer.sh* --> colourBox")
        self.previewImage.set_from_file(self.installDir+"gnome-shell/assets/acid-preview.svg") # set acid-image.svg to new colour
        self.labelImage.set_from_file(self.installDir+"gnome-shell/assets/acid-label.svg") # set acid-image.svg to new colour
        os.environ["tempcolour"] = os.environ["acidcolour"] #store box colour
        os.environ["acidcolour"] = os.environ["oldcolour"] #set new colour to original
        os.environ["oldcolour"] = os.environ["tempcolour"] #set replaced colour to box
        os.system(self.installDir+'configurator/colour-changer.sh') # change theme back to previous
        os.environ["oldcolour"] = os.environ["acidcolour"] # revert replaced colour
        os.environ["acidcolour"] = os.environ["tempcolour"] #acidcolour = box colour
        os.unsetenv("tempcolour") # unset tempcolour
        print ("*Just ran colour-changer.sh* --> oldcolour")
 
    # function to convert colour in self.colourButton to hex code
    def get_colour(self, colourButton):
        newColour = Gdk.RGBA()
        try: #for raring
            newColour = self.colourButton.get_rgba()
        except TypeError: #for quantal
            self.colourButton.get_rgba(newColour)
        code = ""
        for i in (newColour.red, newColour.green, newColour.blue):
            i = hex(int(i*255.0))[2:]
            if len(i) == 1:
                code = code + "0" + i
            else:
                code = code + i
        return code
 
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)
 
    def do_activate(self):
        win = MyWindow(self)
        win.show_all()
 
    def do_startup(self):
        Gtk.Application.do_startup(self)
 
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
 
# TODO - os.unsetenv()
# TODO - colour-switching-proof the SVG(s) --> #rrggbb to rgb(rrr,ggg,bbb)

