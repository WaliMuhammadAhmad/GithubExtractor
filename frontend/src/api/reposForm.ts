import { ref } from 'vue'
import axios from 'axios'

export const useReposForm = () => {
  const reposForm = ref({})

  const reqRepos = async () => {
    console.log(JSON.stringify(reposForm.value, null, 2))
    try {
      const res = axios.post('/repos', JSON.stringify(reposForm.value, null, 2))
      console.log(res)
    } catch (error) {
      console.error(error)
    }
  }

  return { reposForm, reqRepos }
}
