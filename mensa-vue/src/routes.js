// D1. Import the component from the user-components folder.

import menu from './user-components/menu.vue'
import index from './user-components/index.vue'
import test_api from './user-components/test_api.vue'

const routes = [
    // D2. Create the path object which will be used to call the component
    {path:'/test_api', component: test_api},
    {path:'/menu', component:menu},
    {path:'/index', component:index},
    {path:'/', component:index},
];

// D3. Export the routes as default. This will be used when Vue start to render the DOM.
export default routes;
