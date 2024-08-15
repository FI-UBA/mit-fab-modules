#
# panel_path_Roland_SRM_20.py
#    path to Roland SRM-20
#
# Neil Gershenfeld 7/19/14
# (c) Massachusetts Institute of Technology 2014
#
# This work may be reproduced, modified, distributed,
# performed, and displayed for any purpose, but must
# acknowledge the fab modules project. Copyright is
# retained and must be preserved. The work is provided
# as is; no warranty is provided, and users accept all 
# liability.
#
# imports
#
import wx,os,string,threading
#
# panel class
#
class path_Roland_SRM_20_panel(wx.Panel):
   def __init__(self,parent):
      self.parent = parent
      self.parent.path_file = ''
      #
      # make rml
      #
      def make_rml(event):
         if (self.parent.path_file == ''):
            print 'panel_path_Roland_SRM_20: oops -- need path file'
            return
         self.parent.rml_file = self.parent.tmp+self.parent.rootname+'.rml'
         speed = self.speed.GetValue()
         direction = '1'
         zjog = self.zjog.GetValue()
         xmin = self.xmin.GetValue()
         ymin = self.ymin.GetValue()
         command = 'path_rml '+'\"'+self.parent.path_file+'\"'+' '+'\"'+self.parent.rml_file+'\"'+' '+speed+' '+direction+' '+zjog+' '+xmin+' '+ymin
         print command
         os.system(command)
         temp_name = self.parent.tmp+'path_info'
         command = 'path_time '+'\"'+self.parent.path_file+'\"'+' '+speed+' '+zjog+' > '+'\"'+temp_name+'\"'
         print command
         os.system(command)
         output_file = open(temp_name,'r')
         output = output_file.read()
         output_file.close()
         command = 'rm '+'\"'+temp_name+'\"'
         start = 11+string.find(output,'path time: ')
         end = 5+string.find(output,'hours',start)
         times = output[start:end]
         self.info.SetLabel(times)
         self.button.Show()
         self.parent.Layout()
         self.parent.Fit()
      #
      # rml move xy
      #
      def move_rml_xy(event):
         xmin = self.xmin.GetValue()
         ymin = self.ymin.GetValue()
         command = 'rml_move xy '+xmin+' '+ymin+' Roland_SRM-20'
         print command
         os.system(command)
      #
      # rml move z up
      #
      def up_callback():
         global t
         command = 'rml_move zup Roland_SRM-20'
         print command
         os.system(command)
         t = threading.Timer(0.1,up_callback)
         t.start()
      def move_rml_up_start(event):
         global t
         t = threading.Timer(0.1,up_callback)
         t.start()
      def move_rml_up_stop(event):
         global t
         t.cancel()
      #
      # rml move z zero
      #
      def move_rml_zero(event):
         command = 'rml_move z0 Roland_SRM-20'
         print command
         os.system(command)
      #
      # rml move z down
      #
      def down_callback():
         global t
         command = 'rml_move zdown Roland_SRM-20'
         print command
         os.system(command)
         t = threading.Timer(0.1,down_callback)
         t.start()
      def move_rml_down_start(event):
         global t
         t = threading.Timer(0.1,down_callback)
         t.start()
      def move_rml_down_stop(event):
         global t
         t.cancel()
      #
      # send
      #
      def fab_send(event):
         command = 'fab_send '+'\"'+self.parent.rml_file+'\" Roland_SRM-20'
         print command
         os.system(command)
      #
      # panel
      #
      wx.Panel.__init__(self,parent)
      self.sizer = wx.GridBagSizer(10,10)
      self.SetSizer(self.sizer)
      #
      # label
      #
      label = wx.StaticText(self,label='to: Roland SRM-20')
      bold_font = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.BOLD)
      label.SetFont(bold_font)
      self.sizer.Add(label,(0,0),span=(1,2),flag=wx.ALIGN_CENTER_HORIZONTAL)
      #
      # send
      #
      self.button = wx.Button(self,label='send it!')
      self.button.Bind(wx.EVT_BUTTON,fab_send)
      self.button.SetFont(bold_font)
      self.sizer.Add(self.button,(1,0),span=(1,2),flag=(wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL))
      self.button.Hide()
      #
      # info
      #
      self.info = wx.StaticText(self,label="")
      self.sizer.Add(self.info,(2,0),span=(1,2),flag=wx.ALIGN_CENTER_HORIZONTAL)
      #
      # controls
      #
      make = wx.Button(self,label='make .rml')
      make.Bind(wx.EVT_BUTTON,make_rml)
      self.sizer.Add(make,(3,0),span=(1,2),flag=wx.ALIGN_CENTER_HORIZONTAL)
      #
      row4_panel = wx.Panel(self)
      row4_sizer = wx.GridBagSizer(10,10)
      row4_panel.SetSizer(row4_sizer)
      row4_sizer.Add(wx.StaticText(row4_panel,label='speed (mm/s)'),(0,0),flag=wx.ALIGN_CENTER_HORIZONTAL)
      row4_sizer.Add(wx.StaticText(row4_panel,label='jog (mm)      '),(0,1),flag=wx.ALIGN_CENTER_HORIZONTAL)
      self.sizer.Add(row4_panel,(4,0),span=(1,2),flag=(wx.ALIGN_CENTER_HORIZONTAL))
      #
      row5_panel = wx.Panel(self)
      row5_sizer = wx.GridBagSizer(10,10)
      row5_panel.SetSizer(row5_sizer)
      self.speed = wx.TextCtrl(row5_panel,-1,'4')
      row5_sizer.Add(self.speed,(0,0),flag=wx.ALIGN_CENTER_HORIZONTAL)
      self.zjog = wx.TextCtrl(row5_panel,-1,'1')
      row5_sizer.Add(self.zjog,(0,1),flag=wx.ALIGN_CENTER_HORIZONTAL)
      self.sizer.Add(row5_panel,(5,0),span=(1,2),flag=(wx.ALIGN_CENTER_HORIZONTAL))
      #
      row6_panel = wx.Panel(self)
      row6_sizer = wx.GridBagSizer(10,10)
      row6_panel.SetSizer(row6_sizer)
      row6_sizer.Add(wx.StaticText(row6_panel,label='xmin (mm)'),(0,0),flag=wx.ALIGN_CENTER_HORIZONTAL)
      row6_sizer.Add(wx.StaticText(row6_panel,label='ymin (mm)'),(0,1),flag=wx.ALIGN_CENTER_HORIZONTAL)
      self.sizer.Add(row6_panel,(6,0),span=(1,2),flag=(wx.ALIGN_CENTER_HORIZONTAL))
      #
      row7_panel = wx.Panel(self)
      row7_sizer = wx.GridBagSizer(10,10)
      row7_panel.SetSizer(row7_sizer)
      self.xmin = wx.TextCtrl(row7_panel,-1,'20')
      row7_sizer.Add(self.xmin,(0,0),flag=wx.ALIGN_CENTER_HORIZONTAL)
      self.ymin = wx.TextCtrl(row7_panel,-1,'20')
      row7_sizer.Add(self.ymin,(0,1),flag=wx.ALIGN_CENTER_HORIZONTAL)
      self.sizer.Add(row7_panel,(7,0),span=(1,2),flag=(wx.ALIGN_CENTER_HORIZONTAL))
      #
      self.move = wx.Button(self,label='move to xmin,ymin')
      self.move.Bind(wx.EVT_BUTTON,move_rml_xy)
      self.sizer.Add(self.move,(8,0),span=(1,2),flag=wx.ALIGN_CENTER_HORIZONTAL)
      #
      self.zup = wx.Button(self,label='move z up')
      self.zup.Bind(wx.EVT_LEFT_DOWN,move_rml_up_start)
      self.zup.Bind(wx.EVT_LEFT_UP,move_rml_up_stop)
      self.sizer.Add(self.zup,(9,0),span=(1,2),flag=wx.ALIGN_CENTER_HORIZONTAL)
      #
      self.zzero = wx.Button(self,label='zero z')
      self.zzero.Bind(wx.EVT_BUTTON,move_rml_zero)
      self.sizer.Add(self.zzero,(10,0),span=(1,2),flag=wx.ALIGN_CENTER_HORIZONTAL)
      #
      self.zdown = wx.Button(self,label='move z down')
      self.zdown.Bind(wx.EVT_LEFT_DOWN,move_rml_down_start)
      self.zdown.Bind(wx.EVT_LEFT_UP,move_rml_down_stop)
      self.sizer.Add(self.zdown,(11,0),span=(1,2),flag=(wx.ALIGN_CENTER_HORIZONTAL))
      #
      # fit
      #
      self.Fit()
