<template>
  <div class="w-full m-auto flex flex-col items-center relative dark:bg-gray-900">
    <!-- Navbar with two-way dark mode binding -->
    
    <Navbar :darkMode="darkMode" @update:darkMode="darkMode = $event" />
    <div class="container mx-auto">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import { RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'

// Dark mode state with localStorage persistence
const darkMode = ref(localStorage.getItem('theme') === 'dark')

// Watch for dark mode changes and update DOM + localStorage
watchEffect(() => {
  if (darkMode.value) {
    document.documentElement.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
})
</script>

<style scoped>
/* Optional: Keep your existing active link styles if needed */
nav a.router-link-exact-active {
  border-bottom: 2px solid #fff;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

@media (min-width: 1024px) {
  nav {
    text-align: center;
  }
}
</style>