import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useLoadingStore = defineStore('loading', () => {
  const status = ref(false)
  function toggle() {
    status.value = !false
  }

  return { status, toggle }
})
