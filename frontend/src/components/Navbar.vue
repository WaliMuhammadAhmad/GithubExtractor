<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import { RouterLink } from 'vue-router'
defineProps<{
  title: string
}>()
</script>

<template>
  <nav class="navbar">
    <h1 class="title">{{ title }}</h1>
    <div>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/repos">Repos</RouterLink>
      <RouterLink to="/extractor">JUnit Extractor</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  width: 100%;
  min-height: 5dvh;
  padding: 0 1em;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: center;
  box-shadow: 10px 10px 50px 10px var(--color-border);
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1em;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.title {
  color: var(--color-title);
  font-size: 1em;
  font-weight: medium;
  text-transform: uppercase;
  transition: 0.7s ease;
}

.title:hover {
  cursor: auto;
  color: #0cc873;
  box-shadow: #0cc873;
}

@media (max-width: 555px) {
  .navbar {
    flex-direction: column;
    gap: 1em;
  }
}

@media (max-width: 396px) {
  .navbar {
    padding: 0.2em;
  }
  nav a {
    padding: 0 0.5em;
  }
}
</style>
