Even though I was able to make hibernate work in Linux / Kubuntu using a dedicated 34GB parition I was never able to 
integrate it into the Linux frontend. 
I tried but i wasnt able to do it (yet).

So out of necessity was born this pythn program that 
1. Displays a modal dialog box.
2. If user selects yes, then user is prompted for the su password.
3. If password entered then system is hibernated

Please note the following
1. YOu have to make sure that hibernate command works at the cli. 
2. In order to do so, use the comamnd **sudo systemctl hibernate**
3. In order to get to the stage where this command starts working is a whole different ball game. That is your baby.
4. This python program just runs the **sudo systemctl hibernate** from a taskbar icon
5. The following steps for adding this py program to the taskbar
   - kate ~/.local/share/applications/hibernate.desktop
   - Add the following to the .desktop file
      [Desktop Entry]
      Version=1.0
      Type=Application
      Name=Hibernate System
      Comment=Hibernate the compu    ter
      Exec=python3 <exact path to **hibernate.py** file>
      Terminal=true
      Categories=System;
   - Save the file
   - Add it to your taskbar by editing the desktop

 
