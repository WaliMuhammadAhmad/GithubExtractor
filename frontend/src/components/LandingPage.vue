<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <section class="sectionPage">
    <div>
      <h1>Welcome to Github Extractor</h1>
      <p>
        This is a simple web application that allows you to search for Github public repositories
        and a tool to extract Java focal methods and JUnit test cases.
      </p>
    </div>
    <div>
      <img class="logo" src="../assets/logo.svg" alt="logo" />
    </div>
  </section>
</template>

<style scoped>
.sectionPage {
  margin: auto;
  height: 90dvh;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  padding: 0 1rem;
  align-content: center;
  align-items: flex-start;
  justify-items: center;
}
.logo {
  height: auto;
  width: 100%;
}
</style>
