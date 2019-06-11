<template>
    <div>
        Base
    </div>
</template>

<script>
export default {
  data: function () {
    return {
      title: 'My Title'
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
      { name: 'application-name', content: 'Name of my application' },
      { name: 'description', content: 'A description of the page', id: 'desc' }, // id to replace intead of create element
      // ...
 
    ],
    // link tags
    link: [
    //   { rel: 'canonical', href: 'http://example.com/#!/contact/', id: 'canonical' },
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