---
title: "Facilitating Programming-based 3D Computer-Aided Design using Bidirectional Programming"
description: ""
date: 2020-11-01
authors:
  - name: "Gonzalez, J. Felipe" 
    me: true
redirect_link : "https://cil.csit.carleton.ca/bidirectional-programming-csg-cad/"

categories:
  - "Technology"
  - "Research"
  - "HCI"
tags:
  - "HCI"
  - "VR"
  - "Haptics"

draft: false
---


**Hello, designer with a programming background in CAD!** This project is all about making your 3D design experience smoother and more enjoyable, especially if you're the kind of person who loves getting into the code. It's based on my PhD thesis, which you can check out [here](https://hal.science/tel-04635570).


You know how most 3D CAD tools are pretty intuitive, with those drag-and-drop interfaces that let you tweak your designs with ease? Well, there’s another side to CAD—a programming-based approach. Sure, it can seem a bit daunting at first, with all the coding involved, but it opens up some incredible possibilities for your designs. 

<div style="display: flex; flex-wrap: wrap; gap: 10px;">

  <div style="flex: 1 1 45%; max-width: 45%; text-align: center;">
    <a href="https://openscad.org/" target="_blank">
      <img src="/imgs/projects/pr_facilitating/PB_OpenSCAD.png" alt="Programming-based CAD application OpenSCAD" style="width: 100%; height: auto;">
    </a>
    <p>OpenSCAD: A powerful programming-based CAD tool for creating complex 3D models.</p>
  </div>

  <div style="flex: 1 1 45%; max-width: 45%; text-align: center;">
    <a href="https://openjscad.xyz/" target="_blank">
      <img src="/imgs/projects/pr_facilitating/PB_JSCAD.png" alt="Programming-based CAD application JSCAD" style="width: 100%; height: auto;">
    </a>
    <p>JSCAD: A versatile JavaScript-based CAD tool for 3D design and modeling.</p>
  </div>

</div>

The problem is that not many people use it. Why? Mainly because it’s not the easiest thing to get into, and honestly, we don’t fully understand all the challenges that come with it.


That’s why I dove into this research. I wanted to explore the world of programming-based CAD and figure out how to make it more user-friendly, especially for those of you who are into 3D printing and digital fabrication.

### Getting to Know the Users: Challenges Faced by 3D Code Designers

In the first part of my research, I talked to 20 OpenSCAD users—a major tool in the programming-based CAD world. I wanted to get a real sense of what makes this approach challenging. From these conversations, I identified three main areas where users struggle: who the users are, the hurdles they face in 3D design, and the headaches that come up during 3D printing. For example, some users found it tough to visualize how changes in the code would affect the 3D model, while others struggled with the steep learning curve required to master the syntax.

### Bridging the Gap: Making Code and 3D Models Work Together

Next, I tackled a big issue: the tricky relationship between the code and the 3D view. It can be frustrating when you're trying to link what you see on the screen with the lines of code you're writing. To fix this, I introduced the concept of “bidirectional programming.” Now, you can interact with both the code and the view. Imagine this: you’re editing your model directly on the screen, and the code updates automatically. No more switching back and forth or guessing how a code tweak will look. I even tweaked OpenSCAD to make this a reality.

### Simplifying Parametric Design: Making Parametric Design Effortless

Finally, I focused on the challenge of defining geometric properties in parametric designs—a real pain point for many users. For instance, defining the exact dimensions or relationships between different parts of a model can get pretty complex. I analyzed a bunch of OpenSCAD models and developed new features to make it easier to define and manipulate these properties right from the 3D view. When I tested these new features with users, the results were promising. Not only did it make the design process faster and less error-prone, but it also made it much easier for beginners to jump in and start creating.

So, if you’re excited about pushing the limits of 3D design with code, my research is here to make that journey a lot smoother, more intuitive, and definitely more fun!


