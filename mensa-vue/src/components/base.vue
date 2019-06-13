<template>
    <div>
      
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
}
</script>