import { focusInFooter } from './../features/components/footer/focus.js'
import { endAnimation } from './../features/components/main/loadAnimation.js'
import { addScripts, disableTagsA, enableTagsA } from './../SPA-renders/core.js'

document.addEventListener('DOMContentLoaded', useInitialScripts)

function useInitialScripts() {
    focusInFooter()
    setTimeout(endAnimation, 100)
    addScripts([
        ['/static/scripts/features/components/header/hamburguerAnimation.js'],
        ['/static/scripts/features/components/header/inputWidthControl.js'],
        ['/static/scripts/SPA-renders/main/baseMobile.js', true],
        ['/static/scripts/SPA-renders/main/basePC.js', true],
    ])
}