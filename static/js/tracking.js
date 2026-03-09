/**
 * Guardian Landing Pages — GA4 Event Tracking + Form Submission
 *
 * Events tracked:
 * - page_view (automatic via gtag config)
 * - form_submit (lead form filled out)
 * - phone_click (phone number tapped on mobile)
 * - call_received (fired server-side from CallRail webhook via GA4 MP)
 */

// ── Helper: read cookie by name ──────────────────────────────────────
function getCookie(name) {
    var v = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return v ? v.pop() : '';
}

// ── Populate hidden form fields from cookies ─────────────────────────
(function populateHiddenFields() {
    var gclidField = document.getElementById('form-gclid');
    var srcField = document.getElementById('form-utm-source');
    var medField = document.getElementById('form-utm-medium');
    var campField = document.getElementById('form-utm-campaign');
    var termField = document.getElementById('form-utm-term');

    if (gclidField) gclidField.value = getCookie('gclid') || '';
    if (srcField) srcField.value = getCookie('utm_source') || '';
    if (medField) medField.value = getCookie('utm_medium') || '';
    if (campField) campField.value = getCookie('utm_campaign') || '';
    if (termField) termField.value = getCookie('utm_term') || '';
})();

// ── Phone click tracking ─────────────────────────────────────────────
function trackPhoneClick() {
    if (typeof gtag === 'function') {
        gtag('event', 'phone_click', {
            event_category: 'engagement',
            event_label: 'header_phone',
            gclid: getCookie('gclid'),
            value: 1
        });
    }
}

// ── Form submission ──────────────────────────────────────────────────
function submitForm(e) {
    e.preventDefault();
    var form = document.getElementById('lead-form');
    var data = new FormData(form);
    var payload = {};
    data.forEach(function(v, k) { payload[k] = v; });

    // Fire GA4 form_submit event
    if (typeof gtag === 'function') {
        gtag('event', 'form_submit', {
            event_category: 'conversion',
            event_label: payload.service || 'unknown',
            gclid: getCookie('gclid'),
            product: payload.product || '',
            geo: payload.geo || '',
            value: 1
        });
    }

    // Send to webhook endpoint on GuardianQA
    fetch('https://web-production-adfe7.up.railway.app/api/landing-page/lead', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    }).then(function() {
        form.style.display = 'none';
        document.getElementById('form-success').style.display = 'block';
    }).catch(function() {
        // Still show success — we don't want to block the user
        form.style.display = 'none';
        document.getElementById('form-success').style.display = 'block';
    });

    return false;
}
