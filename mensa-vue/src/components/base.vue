<template>
    <div>
        Base
    </div>
</template>

<script>
export default {
  data: function () {
    return {
      title: 'Mensa-Online'
    }
  },
  // Usage with context the component
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
        {rel:"stylesheet", href:"./static/css/main.css"}

    ],
    script: [
    //   { type: 'text/javascript', src: 'cdn/to/script.js', async: true, body: true}, // Insert in body
    ],
    style: [
    //   { type: 'text/css', inner: 'body { background-color: #000; color: #fff}', undo: false },
 
    ]
  }
  
}
</script>