import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ReposView from '../views/ReposView.vue'
import ExtractorView from '../views/ExtractorView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/repos',
      name: 'repos',
      component: ReposView,
    },
    {
      path: '/extractor',
      name: 'extractor',
      component: ExtractorView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
