<template>
    <div
        class="rounded-xl border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 shadow-2xl overflow-hidden transition-all duration-300 hover:shadow-[0_10px_30px_-5px_rgba(99,102,241,0.3)]">
        <!-- Toolbar with futuristic design -->
        <div
            class="flex flex-wrap items-center gap-1 p-2 border-b dark:border-gray-700 bg-gradient-to-r from-gray-50 to-gray-100 dark:from-gray-700 dark:to-gray-800">
            <!-- Text Formatting -->
            <div class="flex">
                <button @click="toggleBold" :class="buttonClass('bold')" class="group relative" aria-label="Bold">
                    <span class="flex items-center justify-center w-12 h-8 font-medium">
                        B
                    </span>
                    <span class="tooltip">Bold (⌘B)</span>
                </button>

                <button @click="toggleItalic" :class="buttonClass('italic')" class="group relative" aria-label="Italic">
                    <span class="flex items-center justify-center w-12 h-8 italic font-medium">
                        I
                    </span>
                    <span class="tooltip">Italic (⌘I)</span>
                </button>

                <button @click="toggleUnderline" :class="buttonClass('underline')" class="group relative"
                    aria-label="Underline">
                    <span class="flex items-center justify-center w-12 h-8 underline font-medium">
                        U
                    </span>
                    <span class="tooltip">Underline (⌘U)</span>
                </button>
            </div>

            <!-- Lists -->
            <div class="flex items-center space-x-1 mr-2">
                <button @click="toggleBulletList" :class="buttonClass('bulletList')" class="group relative"
                    aria-label="Bullet List">
                    <span class="flex items-center justify-center w-8 h-8">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    <span class="tooltip">Bullet List</span>
                </button>

                <button @click="toggleOrderedList" :class="buttonClass('orderedList')" class="group relative"
                    aria-label="Numbered List">
                    <span class="flex items-center justify-center w-8 h-8">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M5 4a1 1 0 00-1 1v1a1 1 0 001 1h1a1 1 0 001-1V5a1 1 0 00-1-1H5zm5 0a1 1 0 00-1 1v1a1 1 0 001 1h1a1 1 0 001-1V5a1 1 0 00-1-1h-1zM5 9a1 1 0 00-1 1v1a1 1 0 001 1h1a1 1 0 001-1v-1a1 1 0 00-1-1H5zm5 0a1 1 0 00-1 1v1a1 1 0 001 1h1a1 1 0 001-1v-1a1 1 0 00-1-1h-1zM5 14a1 1 0 00-1 1v1a1 1 0 001 1h1a1 1 0 001-1v-1a1 1 0 00-1-1H5zm5 0a1 1 0 00-1 1v1a1 1 0 001 1h1a1 1 0 001-1v-1a1 1 0 00-1-1h-1z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    <span class="tooltip">Numbered List</span>
                </button>
            </div>

            <!-- Headings -->
            <div class="flex items-center space-x-1 mr-2">
                <button @click="setHeading(1)" :class="buttonClass('heading', { level: 1 })" class="group relative"
                    aria-label="Heading 1">
                    <span class="flex items-center justify-center w-8 h-8">
                        <span class="font-bold">H1</span>
                    </span>
                    <span class="tooltip">Heading 1</span>
                </button>

                <button @click="setHeading(2)" :class="buttonClass('heading', { level: 2 })" class="group relative"
                    aria-label="Heading 2">
                    <span class="flex items-center justify-center w-8 h-8">
                        <span class="font-bold">H2</span>
                    </span>
                    <span class="tooltip">Heading 2</span>
                </button>

                <button @click="setHeading(3)" :class="buttonClass('heading', { level: 3 })" class="group relative"
                    aria-label="Heading 3">
                    <span class="flex items-center justify-center w-8 h-8">
                        <span class="font-bold">H3</span>
                    </span>
                    <span class="tooltip">Heading 3</span>
                </button>
            </div>

            <!-- Text Alignment -->
            <div class="flex items-center space-x-1 mr-2">
                <button @click="setTextAlign('left')" :class="buttonClass('textAlign', { align: 'left' })"
                    class="group relative" aria-label="Align Left">
                    <span class="flex items-center justify-center w-8 h-8">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    <span class="tooltip">Align Left</span>
                </button>

                <button @click="setTextAlign('center')" :class="buttonClass('textAlign', { align: 'center' })"
                    class="group relative" aria-label="Align Center">
                    <span class="flex items-center justify-center w-8 h-8">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M4 5a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zm2 5a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm-2 5a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    <span class="tooltip">Align Center</span>
                </button>

                <button @click="setTextAlign('right')" :class="buttonClass('textAlign', { align: 'right' })"
                    class="group relative" aria-label="Align Right">
                    <span class="flex items-center justify-center w-8 h-8">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3 5a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm-3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    <span class="tooltip">Align Right</span>
                </button>
            </div>

            <!-- More formatting options -->
            <div class="flex items-center space-x-1">
                <button @click="toggleBlockquote" :class="buttonClass('blockquote')" class="group relative"
                    aria-label="Blockquote">
                    <span class="flex items-center justify-center w-8 h-8">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    <span class="tooltip">Blockquote</span>
                </button>

                <button @click="toggleCodeBlock" :class="buttonClass('codeBlock')" class="group relative"
                    aria-label="Code Block">
                    <span class="flex items-center justify-center w-8 h-8">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z"
                                clip-rule="evenodd" />
                        </svg>
                    </span>
                    <span class="tooltip">Code Block</span>
                </button>

                <button @click="setHorizontalRule"
                    class="group relative flex items-center justify-center w-8 h-8 rounded hover:bg-gray-200 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-300"
                    aria-label="Horizontal Rule">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd"
                            d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                            clip-rule="evenodd" />
                    </svg>
                    <span class="tooltip">Horizontal Rule</span>
                </button>
            </div>
        </div>


        <!-- Editor Content -->
        <div class="bg-gray-100 dark:bg-gray-800 p-4 rounded-lg text-gray-900 dark:text-gray-100">
            <EditorContent :editor="editor"
                class="whitespace-pre-wrap outline-none prose dark:prose-invert max-w-full" />
        </div>

        <!-- <EditorContent 
      :editor="editor" 
      class="p-4 text-gray-900 whitespace-pre-wrap dark:text-gray-100 prose dark:prose-invert max-w-none min-h-[400px] focus:outline-none"
    /> -->
    </div>
</template>

<script setup>
import { onBeforeUnmount, watch } from 'vue'
import { Editor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import Underline from '@tiptap/extension-underline'
import Heading from '@tiptap/extension-heading'
import TextAlign from '@tiptap/extension-text-align'
import Blockquote from '@tiptap/extension-blockquote'
import CodeBlock from '@tiptap/extension-code-block'
import HorizontalRule from '@tiptap/extension-horizontal-rule'
import HardBreak from '@tiptap/extension-hard-break'

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const editor = new Editor({
    content: props.modelValue,
    extensions: [
        StarterKit.configure({
            paragraph: {
                HTMLAttributes: {
                    class: 'my-3'
                }
            },
            hardBreak: false
        }),
        Underline,
        HardBreak.extend({
            addKeyboardShortcuts() {
                return {
                    'Shift-Enter': () => this.editor.commands.setHardBreak()
                }
            }
        }),
        Heading.configure({
            levels: [1, 2, 3],
        }),
        TextAlign.configure({
            types: ['heading', 'paragraph'],
        }),
        Blockquote,
        CodeBlock,
        HorizontalRule,
    ],
    editorProps: {
        attributes: {
      class: 'tw:min-h-[300px] tw:outline-none whitespace-pre-wrap',
      spellcheck: 'false',
      style: 'white-space: pre-wrap;' // Critical for preserving formatting
    },
        
    },

    onUpdate: () => {
        const html = editor.getHTML()
            .replace(/<p>/g, '\n<p>')
            .replace(/<\/p>/g, '</p>\n')
        emit('update:modelValue', html)
    }
})

watch(() => props.modelValue, (newValue) => {
    if (editor && editor.getHTML() !== newValue) {
        editor.commands.setContent(newValue)
    }
})

onBeforeUnmount(() => {
    editor?.destroy()
})

// Formatting commands
const toggleBold = () => editor.chain().focus().toggleBold().run()
const toggleItalic = () => editor.chain().focus().toggleItalic().run()
const toggleUnderline = () => editor.chain().focus().toggleUnderline().run()
const toggleBulletList = () => editor.chain().focus().toggleBulletList().run()
const toggleOrderedList = () => editor.chain().focus().toggleOrderedList().run()
const toggleBlockquote = () => editor.chain().focus().toggleBlockquote().run()
const toggleCodeBlock = () => editor.chain().focus().toggleCodeBlock().run()
const setHorizontalRule = () => editor.chain().focus().setHorizontalRule().run()

const setHeading = (level) => {
    editor.chain().focus().toggleHeading({ level }).run()
}

const setTextAlign = (align) => {
    editor.chain().focus().setTextAlign(align).run()
}

const buttonClass = (type, attributes = {}) => {
    const isActive = editor.isActive(type, attributes)
    return [
        'flex items-center justify-center rounded transition-all duration-200',
        isActive
            ? 'bg-indigo-600 text-white shadow-md'
            : 'bg-transparent text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700',
        'group relative',
        type === 'bold' || type === 'italic' || type === 'underline' ? 'px-2 w-auto' : 'w-8 h-8'
    ]
}
</script>

<style scoped>
/* Tooltips */
.tooltip {
    @apply absolute hidden group-hover:block bg-gray-900 text-white text-xs py-1 px-2 rounded whitespace-nowrap;
    top: -35px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 100;
}

.tooltip::after {
    @apply absolute w-2 h-2 bg-gray-900;
    content: '';
    bottom: -4px;
    left: 50%;
    transform: translateX(-50%) rotate(45deg);
}
</style>

<style>
/* Editor styles */
.ProseMirror {
    @apply min-h-[200px] focus:outline-none;
}

.ProseMirror h1 {
    @apply text-3xl font-bold my-4;
}

.ProseMirror h2 {
    @apply text-2xl font-bold my-3;
}

.ProseMirror h3 {
    @apply text-xl font-bold my-2;
}

.ProseMirror p {
    @apply my-2;
}

.ProseMirror ul,
.ProseMirror ol {
    @apply pl-5 my-2;
}

.ProseMirror ul {
    @apply list-disc;
}

.ProseMirror ol {
    @apply list-decimal;
}

.ProseMirror blockquote {
    @apply border-l-4 border-gray-300 dark:border-gray-600 pl-4 my-2 italic;
}

.ProseMirror pre {
    @apply bg-gray-800 text-gray-100 p-4 rounded my-2 overflow-x-auto;
}

.ProseMirror hr {
    @apply border-t border-gray-300 dark:border-gray-600 my-4;
}

/* Custom scrollbar for editor */
.ProseMirror {
    scrollbar-width: thin;
    scrollbar-color: #6366f1 rgba(255, 255, 255, 0.1);
}

.ProseMirror::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}

.ProseMirror::-webkit-scrollbar-track {
    @apply bg-gray-100 dark:bg-gray-700;
}

.ProseMirror::-webkit-scrollbar-thumb {
    @apply bg-indigo-500 rounded-full;
}

.ProseMirror::-webkit-scrollbar-thumb:hover {
    @apply bg-indigo-600;
}
</style>