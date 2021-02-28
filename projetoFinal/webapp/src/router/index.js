import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'

import helpers from '../helpers/helpers'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }
  ],
  base: '/',
  mode: 'history'
})

router.beforeEach((to, from, next) => {
  document.title = `${helpers.startCase(to.name)} - ${process.env.APP_NAME}`

  next()
})

export default router
