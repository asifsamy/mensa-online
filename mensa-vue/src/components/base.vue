<template>
    <div>
      
        <cheader></cheader>
        <cbanner></cbanner>

        <!-- Set the content of the website herer -->
        
        <cmenu></cmenu>
        <cfooter></cfooter>

    </div>
</template>

<script>

// Import components
import header from './common/header.vue'
import banner from './common/banner.vue'
import footer from './common/footer.vue'
import menu from './menu.vue'

export default {
  components:{
    'cheader':header,
    'cbanner':banner,
    'cfooter':footer,
    'cmenu':menu,
  },
  data: function () {
    return {
   
    }
  },

}
</script>