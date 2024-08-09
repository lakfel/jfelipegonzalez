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
draft: false
---


Working with 3D Computer-Aided Design (CAD) can be incredibly powerful, especially when you dive into the world of programming-based tools. But let’s face it—while these tools offer flexibility, they also come with their own set of challenges. Unlike traditional drag-and-drop CAD interfaces, scripting in a tool like OpenSCAD can be tricky. Simple tasks, like moving an element in 3D space, can become complex and frustrating when you’re just dealing with code.

So, what if you could have the best of both worlds? That’s exactly what I explored in my research. I introduced the concept of bidirectional programming for Constructive Solid Geometry (CSG) CAD tools. This approach allows you to work seamlessly between the code and the 3D view. Imagine being able to navigate and edit your 3D model using either the code or a direct manipulation interface, with the system keeping everything in sync. Sounds cool, right?

To understand the real-world challenges, I interviewed users of OpenSCAD, a popular programming-based CAD tool. I discovered that while users appreciate the precision and flexibility of scripting, they often struggle with spatial transformations and code navigation. They also tend to rely on trial-and-error to make adjustments, which can be time-consuming and cumbersome.

With these insights, I developed a proof-of-concept implementation that integrates bidirectional programming into OpenSCAD. This new approach allows users to interact with their models more intuitively by linking code changes directly with visual updates. I also conducted a detailed walkthrough to show how these new features address the difficulties observed in the study.

The feedback was positive—users found the bidirectional programming concept intriguing and useful, particularly in handling complex design tasks. While there’s still room for improvement, this work paves the way for more intuitive and effective tools in 3D CAD design.

Dive into the details of this research to see how bidirectional programming can transform your 3D design experience!