# Ex.08 Design of Interactive Image Gallery
## Date:18/12/2024

## AIM:
To design a web application for an inteactive image gallery with minimum five images.

## DESIGN STEPS:

### Step 1:
Clone the github repository and create Django admin interface.

### Step 2:
Change settings.py file to allow request from all hosts.

### Step 3:
Use CSS for positioning and styling.

### Step 4:
Write JavaScript program for implementing interactivity.

### Step 5:
Validate the HTML and CSS code.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
<html >
  <head>
   
    <title>Image Gallery</title>
    
    <style>
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }

        body {
          background: #ecf4fb;
        }

        .img-gallery {
          width: 80%;
          margin: 100px auto 50px;
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          grid-gap: 30px;
        }

        .img-gallery img {
          width: 100%;
          cursor: pointer;
          transition: 1s ease;
        }

        .img-gallery img:hover {
          transform: scale(0.8);
          box-shadow: 0 32px 75px rgba(68, 77, 136, 0.2);
        }

        /* Wrapper */
        .imageWrapper {
          width: 100%;
          height: 100vh;
          background: rgba(0, 0, 0, 0.9);
          position: fixed;
          top: 0;
          left: 0;
          display: none;
          justify-content: center;
          align-items: center;
          z-index: 100;
        }

        .imageWrapper img {
          width: 90%;
          max-width: 500px;
        }

        .imageWrapper span {
          position: absolute;
          top: 5%;
          right: 5%;
          font-size: 30px;
          font-family: sans-serif;
          color: #fff;
          cursor: pointer;
        }
    </style>
  </head>
  <body>
    <!-- Modal Wrapper -->
    <div class="imageWrapper" id="wrapper">
      <img src="images/Img1.jpg" id="fullImg" />
      <span>X</span>
    </div>

    <!-- Gallery -->
    <div class="img-gallery">
      <img src="img1.jpg" />
      <img src="img2.jpg" />
      <img src="img3.jpg" />
      <img src="img4.jpg" />
      <img src="img5.jpg" />
    </div>

    <script>
      // Get all image elements in the gallery
      let images = document.querySelectorAll(".img-gallery img");
      let wrapper = document.getElementById("wrapper");
      let imgWrapper = document.getElementById("fullImg");
      let close = document.querySelector("#wrapper span"); 

      // Loop through each image and add click event
      images.forEach((img, index) => {
        img.addEventListener("click", () => {
          openModal(`img${index + 1}.jpg`);
        });
      });

     
      close.addEventListener("click", () => {
        wrapper.style.display = "none";
      });

      function openModal(pic) {
        wrapper.style.display = "flex";
        imgWrapper.src = pic; // Update the source of the modal image
      }
    </script>
  </body>
</html>

```

## OUTPUT:
![alt text](<Screenshot (135)-1.png>)
![alt text](<Screenshot (136).png>)
![alt text](<Screenshot (137).png>)
![alt text](<Screenshot (138).png>)
![alt text](<Screenshot (139).png>)
![alt text](<Screenshot (140).png>)

## RESULT:
The program for designing an interactive image gallery using HTML, CSS and JavaScript is executed successfully.
