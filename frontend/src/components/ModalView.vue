<script setup>
import { defineEmits, ref, watch } from 'vue'
import { useReposForm } from '@/api/reposForm'
import LoadingIcon from './icons/LoadingIcon.vue'
import { useLoadingStore } from '@/stores/status'
import Papa from 'papaparse'

const { csvLink } = useReposForm()
const { status } = useLoadingStore()
const emit = defineEmits(['close'])

const csvData = ref([])
console.log(status)
const closeModal = () => {
  emit('close')
}

const fetchCSV = async () => {
  if (!csvLink.value) return

  try {
    const response = await fetch(csvLink.value)
    const csvText = await response.text()

    Papa.parse(csvText, {
      header: true,
      skipEmptyLines: true,
      complete: (result) => {
        csvData.value = result.data
      },
    })
  } catch (error) {
    console.error('Error fetching CSV:', error)
  }
}

// Watch for changes in `csvLink` and fetch CSV data
watch(csvLink, fetchCSV)

// Function to download CSV
const downloadCSV = () => {
  if (!csvLink.value) return
  const link = document.createElement('a')
  link.href = csvLink.value
  link.download = 'repos.csv'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}
</script>

<template>
  <section class="modal">
    <div class="modalBody">
      <button @click="closeModal" class="close" style="align-self: flex-end">Close</button>
      <h1>Download the repos list in CSV</h1>
      <div>Please wait while the file is being generated. Once ready, you can download it.</div>

      <div v-if="!status"><LoadingIcon /></div>

      <div class="csv">
        <div v-if="!status" class="csvInfo">
          <p>File Name:</p>
          <p>File Size:</p>
        </div>

        <!-- CSV Table -->
        <div v-if="csvData.length">
          <table>
            <thead>
              <tr>
                <th v-for="(value, key) in csvData[0]" :key="key">{{ key }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in csvData" :key="index">
                <td v-for="(value, key) in row" :key="key">{{ value }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p v-else>No data available</p>

        <!-- Download Button -->
        <button class="button" @click="downloadCSV">Download</button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.modal {
  opacity: 0.9;
  height: 100dvh;
  width: 100%;
  background-color: black;
  position: fixed;
  top: 0;
  left: 0;
}

.modalBody {
  opacity: 1;
  height: 85dvh;
  width: 90%;
  margin: 2em auto 0 auto;
  background-color: #043221;
  border: 2px solid hsla(160, 100%, 37%, 0.2);
  box-shadow: 2em 2em 2em hsla(160, 100%, 37%, 0.2);
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: wrap;
  align-content: space-around;
  gap: 0.2rem;
  padding: 0.5em 1em;
  font-size: 1.5rem;
}

button {
  width: fit-content;
  background-color: hsla(160, 100%, 37%, 0.2);
  color: white;
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

button:hover {
  background-color: hsla(160, 100%, 37%, 0.4);
}

.csv {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1em;
  align-items: center;
}

.csvInfo {
  width: 100%;
  display: flex;
  justify-content: space-evenly;
}

/* Table Styling */
table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  color: black;
}

th,
td {
  padding: 8px;
  border: 1px solid black;
}

th {
  background: hsla(160, 100%, 37%, 0.3);
}
</style>
