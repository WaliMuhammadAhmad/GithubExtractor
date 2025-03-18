import { ref } from 'vue'
import axios from 'axios'
import { useLoadingStore } from '@/stores/status'

export const useReposForm = () => {
  const { status, toggle } = useLoadingStore()
  const reposForm = ref({})
  const csvLink = ref<string | null>(null) // Store CSV link

  const reqRepos = async () => {
    console.log(JSON.stringify(reposForm.value, null, 2))
    if (!status) toggle()

    try {
      const response = await axios.post('/repos', JSON.stringify(reposForm.value, null, 2))
      console.log(response)

      // Assuming response.data contains the CSV URL
      csvLink.value = response.data.csv_url
    } catch (error) {
      console.error(error)
    } finally {
      toggle()
    }
  }

  return { reposForm, reqRepos, csvLink }
}
