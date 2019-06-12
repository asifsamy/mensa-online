<template>
    <div lang="zxx" class="no-js">
        Base
        <cheader></cheader>
        <cbanner></cbanner>
        <cfooter></cfooter>
    </div>
</template>

<script>

// Import components
import header from './common/header.vue'
import banner from './common/banner.vue'
import footer from './common/footer.vue'

export default {
  components:{
    'cheader':header,
    'cbanner':banner,
    'cfooter':footer,
  },
  data: function () {
    return {
      title: 'Mensa-Online'
    }
  },
  // head of the HTML file



  // Meta tags
  head: {
    // To use "this" in the component, it is necessary to return the object through a function
    title: function () {
      return {
        inner: this.title
      }
    },
    meta: [
    //   { name: 'description', content: 'My description', id: 'desc' }
        // <!-- Mobile Specific Meta -->
        {name: name="viewport", content: "width=device-width, initial-scale=1, shrink-to-fit=no"},
        // <!-- Author Meta -->
		    {name:"author", content:"colorlib"},
        // <!-- Meta Description -->
        {name:"description", content:""},
        // <!-- Meta Keyword -->
        {name:"keywords", content:""},
        // <!-- meta character set -->
		// {charset="UTF-8"},
    ],
    // link tags
    link: [
        {href:"https://fonts.googleapis.com/css?family=Poppins:100,200,400,300,500,600,700", rel:"stylesheet"},
        {rel:"stylesheet", href:"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"},
        
        // CSS
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/main.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/linearicons.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/font-awesome.min.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/bootstrap.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/magnific-popup.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/jquery-ui.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/nice-select.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/animate.min.css", async: true, body: true},
        {rel:"stylesheet", type:"text/html",href:"/common/static/css/owl.carousel.css", async: true, body: true},
    ],
  
    script: [
      
      {type: 'text/javascript', src: '/src/components/common/static/js/vendor/jquery-2.2.4.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/popper.min.js', async: true, body: true},
      // {type: 'text/javascript', src: '/src/components/common/static/js/vendor/bootstrap.min.js', async: true, body: true},
      // {type: 'text/javascript', src: 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBhOdIF3Y9382fqJYt5I_sswSrEw5eihAA', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/jquery-ui.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/easing.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/hoverIntent.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/superfish.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/jquery.ajaxchimp.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/jquery.magnific-popup.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/jquery.nice-select.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/owl.carousel.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/isotope.pkgd.min.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/mail-script.js', async: true, body: true},
      {type: 'text/javascript', src: '/src/components/common/static/js/main.js', async: true, body: true}, // Insert in body
    

    ],
    style: [
    //   { type: 'text/css', inner: 'body { background-color: #000; color: #fff}', undo: false },
 
    ]
  }
  
}
</script>