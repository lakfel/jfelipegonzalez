---
title: "Introducing Bidirectional Programming in Constructive Solid Geometry-Based CAD"
title_list: "Bridging the Gap: Making Code and 3D Models Work Together"
order: 2
description_list: "I tackled a big issue in programming-based CAD: the tricky relationship between the code and the 3D view. It can be frustrating when you're trying to link what you see on the screen with the lines of code you're writing. To fix this, I introduced the concept of “bidirectional programming” into CAD. Now, you can interact with both the code and the view. Imagine this: you’re editing your model directly on the screen, and the code updates automatically. No more switching back and forth or guessing how a code tweak will look. I even tweaked OpenSCAD to make this a reality."
video: "/videos/2023_SUI_Introducing.mp4"
type: "projects"
date: 2020-11-01
authors:
  - name: "Gonzalez, J. Felipe" 
    me: true
categories:
  - "Technology"
  - "Research"
  - "HCI"
tags:
  - "HCI"
  - "CAD"
project: "pr_facilitating_programming-based_cad"
subproject: "spr1_understanding"
layout : "single"
publications:
  - "2023_sui_introducing"
todo:
  - Improve description with videos
  - Link with the Github development made by Damien Marchal
draft: false
---


Programming-based CAD applications are powerful, but they come with challenges. Unlike traditional drag-and-drop interfaces, scripting in tools like OpenSCAD can be frustrating, especially when trying to locate specific parts of the model in the code or move an element in 3D space.

In this project, I introduced bidirectional programming for Constructive Solid Geometry (CSG) CAD tools. This approach lets you seamlessly switch between coding and the 3D view, allowing for easy navigation and editing. Imagine editing your 3D model through code or direct manipulation, with the system keeping everything in sync.

I developed a proof-of-concept for <a href="https://openscad.org/" target="_blank">OpenSCAD</a>, addressing two key issues: code navigation and simple spatial transformations. This method links code changes directly with visual updates, making model interaction more intuitive. A detailed walkthrough demonstrates how these features simplify complex design tasks.

Feedback has been positive—users find the bidirectional programming concept both intriguing and practical. While there’s room for improvement, this work lays the groundwork for more intuitive and efficient 3D CAD tools.

# Bidirectional Programming in Constructive Solid Geometry-Based CAD

I aimed to introduce the concept of *Bidirectional Programming* in programming-based CAD thorugh a proof-of-concept developed in OpenSCAD. Specifically, I have integrated navigation and editing features through interactions with the view.

## Getting started

The process of making the code and issuing a pull request on the OpenSCAD repository is on the way. In the mean while, we have a beta version for **MacOS** devices available in the next [link](https://nextcloud.univ-lille.fr/index.php/s/4D8aa9L6JE5rTDp).

### Start the application 

This version of OpenSCAD is under development and it does not have a Developer ID certificate. Thus, when you try to run it, a warning message indicates that the system can not open the application because it cannot confirm the developer’s identity (Fig. 1).

<div class="image-container">
  <div class="image-item">
      <img style= "max-width: 300px "src="/imgs/projects/pr_facilitating/spr1_introducing/imgNoOpen.png" alt="Fig1. Error message when starting the app">
    <p>Fig1. Error message when starting the app</p>
  </div>
</div>

You can do a secondary click (typically a two fingers tap or a right click). The system will display an options list. Select the option “Open” (Fig. 2). A pop-up will appear asking for confirmation of this action. Confirm by pressing the “Open” button.

<div class="image-container">
  <div class="image-item">
      <img style= "max-width: 250px "src="/imgs/projects/pr_facilitating/spr1_introducing/imgRightClick.png" alt="Fig 2. Secondary click on the app to open it">
    <p>Fig 2. Secondary click on the app to open it</p>
  </div>
  <div class="image-item">
      <img style= "max-width: 250px "src="/imgs/projects/pr_facilitating/spr1_introducing/imgO.png" alt="Fig 3. Click on open button">
    <p>Fig 3. Click on open button</p>
  </div>
</div>

You will see the normal OpenSCAD interface.

# Bidirectional Programming Features

I have implemented two sets of features: Navigation and Editing. Please activate both features before start

## Activating

Typically, the settings for editing from the view are set by default. You should see at the bottom of the View Area three new buttons: ``Translate``, ``Rotate``, and ``Scale``. If not, go to `` settings -> editor ``. Scroll down and find the options ``Enable direct manipulation`` and ``Highlight Edges when you select an object``. Check them. If they are already checked, uncheck them, and recheck them. The system should have placed the buttons previously mentioned in the view area.

<div class="image-container">
  <div class="image-item">
      <img style= "max-width: 450px "src="/imgs/projects/pr_facilitating/spr1_introducing/settings-1.png" alt="Fig 4. Enabling direct manipulation on settings window, editor tab.">
    <p>Fig 4. Enabling direct manipulation on settings window, editor tab.</p>
  </div>
</div>

 ## Navigation

 I developed a series of features to assist users in understanding how the code is related to the elements in the view.

 ## Reverse search

 The original version of OpenSCAD allows right-clicking on the view elements to display a list of the code statements contributing to creating that part. In our OpenSCAD version, when you hover over the different items on the list, the system will mark that element as ***the target***. The program colors green the edges of the target. It also highlights the code statement, including its scope, that creates the target in the same color. The system highlights in green the code statements of the call stack involved in the target. It adds a number on the editor’s margins to follow the target’s stack order.

 <div class="image-container">
  <div class="image-item">
      <img style= "max-width: 750px "src="/imgs/projects/pr_facilitating/spr1_introducing/navigating-1536x960.png" alt="Fig 5. Selecting an object after right-clicking on it. Users can hover over the items in the list while the system shows visual feedback connecting the code with the view.">
    <p>Fig 5. Selecting an object after right-clicking on it. Users can hover over the items in the list while the system shows visual feedback connecting the code with the view.</p>
  </div>
</div>

Suppose the code statement of the target creates other elements in the view (for instance, a code statement inside a loop or in a module instantiated several times). In that case, these elements are marked as ***impacted***. The system colors pink the edges of impacted elements in the view. Consequently, the code statements in the editor are colored pink. If the target part is created by a difference or an intersect statement, the system adds colored ghosts of the removed part in the target and impacted elements. The user can now right-click on the ghost to explore their code, just like the other parts.

## Forward search

The user can also search elements from the code editor. By selecting at least two text characters and pressing the key ``F1``, the system will locate the parts in the view created by the code statement. If only one, the system will mark the part as the target. Otherwise, all elements will be marked as impacted. If the user selects the text of variable definitions, the system will find all the elements impacted by the variable and will mark the impacted. The system will color the edges, create ghosts, and highlight the code, as it is described in the reverse search.

# Editing

The system allows users to perform some edits directly from the view.

## Performing edits

To edit the view, you must first select the element you want to edit. You can do it by marking an element as a target using the Reverse search feature explained previously. Then, you can select between the three available buttons to perform the spatial edits of *Translate*, *Rotate*, and *Scale*.

 <div class="image-container">
  <div class="image-item">
      <img style= "max-width: 750px "src="/imgs/projects/pr_facilitating/spr1_introducing/rotateActivate-1024x640.png" alt="Fig 6. After selecting an element, press the operation button at the right bottom of the view area. In this case Rotate button">
    <p>Fig 6. After selecting an element, press the operation button at the right bottom of the view area. In this case Rotate button</p>
  </div>
</div>

After clicking, the system places a widget representing the three axes (X,Y, and Z) in the center of the target object. You must select the axis you want to edit by clicking on it. The widget will turn opaque purple, indicating you are in editing mode.


 <div class="image-container">
  <div class="image-item">
      <img style= "max-width: 750px "src="/imgs/projects/pr_facilitating/spr1_introducing/rotateAxisSelected-1024x640.png" alt="Fig 7. Click the widget of the axis you want to modify. The purple color indicates you are in editing mode">
    <p>Fig 7. Click the widget of the axis you want to modify. The purple color indicates you are in editing mode</p>
  </div>
</div>

## Limitations

This is a project in development and as such it has some limitations. We are currently working to partially integratint this features in OpenSCAD.

### Only one-file models
Currently, interactive features ONLY work with models scripted in one file

### Constraints editing not supported… yet
Currently, the system does not support making edits on statements with variable-based constraints. When trying to edit one, the system will not perform any action.

### Previous versions
For checking previous versions visit this [link](https://nextcloud.univ-lille.fr/index.php/s/5mpHrFtfbrMGDS4).