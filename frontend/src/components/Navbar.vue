<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <nav
        class="w-full bg-white/80 dark:bg-gray-800/80 z-[80] sticky top-0 backdrop-blur-lg px-4 border-b border-gray-200 dark:border-gray-700 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <img class=" w-28 h-10 text-xl" src="../assets/logo2.png" />
                        <!-- <span
                            class="text-xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent dark:from-blue-400 dark:to-purple-400">
                            Corehotech AI
                        </span> -->
                    </div>

                    <!-- Single Desktop Menu Item -->
                </div>
                <!-- <div class="hidden lg:flex ml-10">
                    <div class="relative group"> -->
                        <!-- More Button -->
                        <!-- <button @click="toggleMegaMenu(0)"
                            class=" py-2 text-sm font-medium text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-all duration-200 flex items-center"
                            :class="{ 'text-blue-600 dark:text-blue-400': activeMegaMenu === 0 }">
                            More
                            <svg class="w-4 h-4 ml-1 transition-transform duration-200"
                                :class="{ 'rotate-180': activeMegaMenu === 0 }" fill="none" stroke="currentColor"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M19 9l-7 7-7-7" />
                            </svg>
                        </button> -->

                        <!-- Mega Menu Dropdown -->
                        <!-- <div v-if="activeMegaMenu === 0"
                            class="absolute left-1/2 transform -translate-x-1/2 w-[90vw] max-w-[400px] mt-2 z-50 px-2 pt-2"
                            @mouseleave="activeMegaMenu = null">
                            <div
                                class="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 dark:bg-gray-800 bg-white overflow-hidden">
                                <div class="relative grid gap-2 p-2 sm:grid-cols-1 md:grid-cols-2">
                                    <div v-for="(subItem, subIndex) in navItems[0].subItems" :key="subIndex"
                                        class="group relative rounded-lg p-2 transition-colors duration-150">
                                        <div class="flex items-center">
                                            <div class="ml-4">
                                                <router-link :to="subItem.path"
                                                    class="text-sm font-medium flex gap-1 items-center text-gray-900 dark:text-white hover:text-blue-600 dark:hover:text-blue-400"
                                                    @click="activeMegaMenu = null">
                                                    <component :is="subItem.icon" class="h-4 w-4" />
                                                    {{ subItem.name }}
                                                </router-link>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div> -->
                    <!-- </div>
                </div> -->


                <!-- Right Side Controls -->
                <div class="flex items-center space-x-4">
                    <!-- Support Me Button -->
                    <a href="https://www.buymeacoffee.com/yourusername" target="_blank" rel="noopener noreferrer"
                        class="hidden md:flex items-center px-4 py-2 text-sm font-medium rounded-md shadow-sm text-white bg-gradient-to-r from-blue-600 to-purple-600 transition-all duration-200 group">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 24 24"
                            fill="currentColor">
                            <path
                                d="M18 8h1a3 3 0 010 6h-1v1a5 5 0 01-5 5H7a5 5 0 01-5-5V8h16zm1 4a1 1 0 000-2h-1v2h1zM6 2a1 1 0 011 1v2a1 1 0 11-2 0V3a1 1 0 011-1zm4 0a1 1 0 011 1v2a1 1 0 11-2 0V3a1 1 0 011-1zm4 0a1 1 0 011 1v2a1 1 0 11-2 0V3a1 1 0 011-1z" />
                        </svg>

                        Buy me a coffee
                    </a>

                    <!-- Dark Mode Toggle -->
                    <button @click="$emit('update:darkMode', !darkMode)"
                        class="relative inline-flex items-center h-8 w-16 rounded-full transition-colors duration-300 focus:outline-none"
                        :class="darkMode ? 'bg-gray-600' : 'bg-gray-300'" aria-label="Toggle dark mode">
                        <span
                            class="absolute left-1 inline-block h-6 w-6 transform bg-white rounded-full shadow-md transition-transform duration-300"
                            :class="darkMode ? 'translate-x-8' : 'translate-x-0'">

                            <svg v-if="darkMode" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 p-1 text-gray-700"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
                            </svg>
                            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 p-1 text-gray-700" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
                            </svg>
                        </span>
                    </button>

                    <!-- Mobile Menu Button -->
                    <button @click="isMobileMenuOpen = !isMobileMenuOpen"
                        class="lg:hidden p-2 rounded-md text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        aria-label="Toggle menu">
                        <svg v-if="!isMobileMenuOpen" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                        <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div v-if="isMobileMenuOpen" class="lg:hidden bg-white dark:bg-gray-800 shadow-lg">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <div>
                    <button @click="toggleMobileMenu(0)"
                        class="w-full flex justify-between items-center px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-gray-100 dark:hover:bg-gray-700">
                        Career Tools
                        <svg class="w-4 h-4 ml-1 transition-transform duration-200"
                            :class="{ 'rotate-180': activeMobileMenu === 0 }" fill="none" stroke="currentColor"
                            viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>

                    <div v-if="activeMobileMenu === 0" class="pl-4 space-y-1">
                        <router-link v-for="(subItem, subIndex) in navItems[0].subItems" :key="subIndex"
                            :to="subItem.path"
                            class="block px-3 py-2 rounded-md text-sm font-medium text-gray-600 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-gray-50 dark:hover:bg-gray-700"
                            @click="isMobileMenuOpen = false">
                            {{ subItem.name }}
                        </router-link>
                    </div>
                </div>

                <div class="pt-4 border-t border-gray-200 dark:border-gray-700">
                    <a href="https://www.buymeacoffee.com/yourusername" target="_blank" rel="noopener noreferrer"
                        class="w-full flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-gradient-to-r from-blue-600 to-purple-600">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 24 24"
                            fill="currentColor">
                            <path
                                d="M18 8h1a3 3 0 010 6h-1v1a5 5 0 01-5 5H7a5 5 0 01-5-5V8h16zm1 4a1 1 0 000-2h-1v2h1zM6 2a1 1 0 011 1v2a1 1 0 11-2 0V3a1 1 0 011-1zm4 0a1 1 0 011 1v2a1 1 0 11-2 0V3a1 1 0 011-1zm4 0a1 1 0 011 1v2a1 1 0 11-2 0V3a1 1 0 011-1z" />
                        </svg>
                        Support My Work
                    </a>
                </div>
            </div>
        </div>
    </nav>
</template>

<script setup>
import { ref } from 'vue'
import {
    DocumentTextIcon,
    ChatBubbleLeftRightIcon,
    AcademicCapIcon,
    CogIcon,
} from '@heroicons/vue/24/outline'

defineProps({
    darkMode: {
        type: Boolean,
        required: true
    }
})

// const emit = defineEmits(['update:darkMode'])

const isMobileMenuOpen = ref(false)
// const activeMegaMenu = ref(null)
const activeMobileMenu = ref(null)

// const toggleMegaMenu = (index) => {
//     activeMegaMenu.value = activeMegaMenu.value === index ? null : index
// }

const toggleMobileMenu = (index) => {
    activeMobileMenu.value = activeMobileMenu.value === index ? null : index
}

const navItems = [
    {
        name: 'Career Tools',
        path: '/tools',
        subItems: [
            {
                name: 'Resume Builder',
                path: '/resume-builder',
                icon: DocumentTextIcon
            },
            {
                name: 'Interview Prep',
                path: '/interview-prep',
                icon: ChatBubbleLeftRightIcon
            },
            {
                name: 'Skill Assessment',
                path: '/skill-assessment',
                icon: AcademicCapIcon
            },
            {
                name: 'Salary Calculator',
                path: '/salary-calculator',
                icon: CogIcon
            }
        ]
    }
]
</script>