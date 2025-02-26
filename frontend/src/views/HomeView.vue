<script setup lang="ts">
import { RouterLink } from 'vue-router'
import FixedImage from '@/components/FixedImage.vue'
import Footer from '@/components/Footer.vue'
</script>

<template>
  <div class="container">
    <section class="landingSection">
      <div>
        <h1 class="heading">Welcome to Github Extractor</h1>
        <p>
          This is a simple web application that allows you to search for Github public repositories
          and a tool to extract Java focal methods and JUnit test cases. A tool to make your life
          easier for gathering details of public Github repositories.
        </p>
      </div>
      <div>
        <FixedImage />
      </div>
    </section>
    <section class="restSection">
      <h1>Explore GitHub Repositories Your Way</h1>
      <p>Pick a language, choose a date, and dive into public repository details instantly.</p>
      <RouterLink style="width: fit-content" to="repos"> Get Started </RouterLink>
    </section>
    <section class="restSection">
      <h1>Extract Focal methods and their JUnit test cases</h1>
      <p>
        Automatically extract focal methods and their corresponding JUnit test cases from any Java
        repository on one click.
      </p>
      <RouterLink style="width: fit-content" to="extractor"> Let's Extract </RouterLink>
    </section>
    <section class="restSection">
      <h1>About this Project</h1>
      <p>
        This project was created to simplify the process of exploring and extracting information
        from public GitHub repositories. It leverages the GitHub API to fetch repository data and
        provides tools to extract Java focal methods and their corresponding JUnit test cases.
      </p>
      <RouterLink style="width: fit-content" to="about"> Learn More </RouterLink>
    </section>
  </div>
  <footer>
    <Footer />
  </footer>
</template>

<style scoped>
.landingSection {
  height: 95dvh;
  width: 50dvw;
  display: flex;
  align-items: center;
}
.restSection {
  height: 100dvh;
  width: 50dvw;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
h1 {
  font-size: 2rem;
  font-weight: semibold;
  letter-spacing: -2px;
}
.heading {
  font-size: 4rem;
  letter-spacing: -4px;
  line-height: 1;
  font-weight: bold;
  margin-bottom: 1rem;
}
</style>
